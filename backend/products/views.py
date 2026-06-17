from django.shortcuts import render
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api

from rest_framework import generics, filters
from .models import Product, Category, DeliveryPlace
from .serializers import ProductSerializer, CategorySerializer, ProductUpdateSerializer, CategoryUpdateSerializer, \
    CategoryCreateSerializer, ProductCreateSerializer, DeliveryPlaceSerializer
from accounts.mixins import StaffEditorPermissionMixin, GeneralUserPermissionMixin
from datetime import datetime


# Products
class ProductListSearchView(generics.ListAPIView):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']


class ProductListFilterView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        filters_kwargs = {}
        title = self.request.query_params.get('title')
        if title is not None:
            filters_kwargs['title'] = title
        price = self.request.query_params.get('price')
        if price is not None:
            filters_kwargs['price__lte'] = price
        if self.request.query_params.get('total_stock'):
            total_stock = int(self.request.query_params.get('total_stock'))
            # if total_stock is True:
            #     filters_kwargs['total_stock__gt'] = 0
            if total_stock == 0 or total_stock < 0:
                filters_kwargs['total_stock__lte'] = total_stock
            else:
                filters_kwargs['total_stock__gt'] = 0
        category = self.request.query_params.get('category')
        if category is not None:
            filters_kwargs['category'] = category
        queryset = Product.objects.filter(**filters_kwargs)
        return queryset


class ProductsByCategory(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category = self.kwargs.get('catId')
        queryset = Product.objects.filter(category=category)
        return queryset


class ProductCreateView(StaffEditorPermissionMixin, generics.CreateAPIView):
    queryset = queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer

    def perform_create(self, serializer):
        image_names = {}

        IMG_HEIGHT, IMG_WIDTH = 680, 680

        if 'image1file' in serializer.validated_data:
            image1file = serializer.validated_data.pop('image1file')
            image1_up = cloudinary.uploader.upload(image1file, folder=os.environ.get('CLOUDINARY_CLOUD_FOLDER'),
                                                   width=IMG_WIDTH, height=IMG_HEIGHT, crop="fill")
            image_names['image1'] = image1_up['public_id'] + '.' + image1_up['format']

        if 'image2file' in serializer.validated_data:
            image2file = serializer.validated_data.pop('image2file')
            image2_up = cloudinary.uploader.upload(image2file, folder=os.environ.get('CLOUDINARY_CLOUD_FOLDER'),
                                                   width=IMG_WIDTH, height=IMG_HEIGHT, crop="fill")
            image_names['image2'] = image2_up['public_id'] + '.' + image2_up['format']

        if 'image3file' in serializer.validated_data:
            image3file = serializer.validated_data.pop('image3file')
            image3_up = cloudinary.uploader.upload(image3file, folder=os.environ.get('CLOUDINARY_CLOUD_FOLDER'),
                                                   width=IMG_WIDTH, height=IMG_HEIGHT, crop="fill")
            image_names['image3'] = image3_up['public_id'] + '.' + image3_up['format']

        if 'image4file' in serializer.validated_data:
            image4file = serializer.validated_data.pop('image4file')
            image4_up = cloudinary.uploader.upload(image4file, folder=os.environ.get('CLOUDINARY_CLOUD_FOLDER'),
                                                   width=IMG_WIDTH, height=IMG_HEIGHT, crop="fill")
            image_names['image4'] = image4_up['public_id'] + '.' + image4_up['format']

        instance = serializer.save(**image_names)


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateView(StaffEditorPermissionMixin, generics.UpdateAPIView):
    serializer_class = ProductUpdateSerializer
    queryset = Product.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.title:
            del instance.title


class ProductDeleteView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def perform_destroy(self, instance):
        if instance.image1: cloudinary.uploader.destroy(instance.image1.split('.')[0])
        if instance.image2: cloudinary.uploader.destroy(instance.image2.split('.')[0])
        if instance.image3: cloudinary.uploader.destroy(instance.image3.split('.')[0])
        if instance.image4: cloudinary.uploader.destroy(instance.image4.split('.')[0])
        return super().perform_destroy(instance)


# Categories
class CategoryCreateView(StaffEditorPermissionMixin, generics.CreateAPIView):
    serializer_class = CategoryCreateSerializer
    queryset = Category.objects.all()

    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        categoryimage = serializer.validated_data.pop('categoryimage')
        # Compress image
        upload_response = cloudinary.uploader.upload(categoryimage, folder=os.environ.get('CLOUDINARY_CLOUD_FOLDER'),
                                                     width=200,
                                                     height=200,
                                                     crop="fill")
        image_name = upload_response['public_id'] + '.' + upload_response['format']
        instance = serializer.save(name=name, image=image_name)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateView(StaffEditorPermissionMixin, generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer

    def perform_update(self, serializer):
        instance = serializer.save()


class CategoryDeleteView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        delete_image = cloudinary.uploader.destroy(instance.image.split('.')[0])
        return super().perform_destroy(instance)


class DeliveryChargeCreateView(StaffEditorPermissionMixin, generics.CreateAPIView):
    queryset = DeliveryPlace.objects.all()
    serializer_class = DeliveryPlaceSerializer

    def perform_create(self, serializer):
        serializer.save()


class DeliveryPlaceListView(generics.ListAPIView):
    queryset = DeliveryPlace.objects.all()
    serializer_class = DeliveryPlaceSerializer


class DeliveryPlaceRetrieveView(generics.RetrieveAPIView):
    queryset = DeliveryPlace.objects.all()
    serializer_class = DeliveryPlaceSerializer


class DeliveryPlaceUpdateView(StaffEditorPermissionMixin, generics.UpdateAPIView):
    queryset = DeliveryPlace.objects.all()
    serializer_class = DeliveryPlaceSerializer

    # def perform_update(self, serializer):


class DeliveryPlaceDeleteView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = DeliveryPlace.objects.all()
    serializer_class = DeliveryPlaceSerializer
