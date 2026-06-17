from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.


class Category(MPTTModel):
    name = models.CharField(blank=False, null=False, unique=True, max_length=100)
    parent = TreeForeignKey(
        "self", null=True, blank=True, related_name="children", on_delete=models.SET_NULL
    )
    image = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shipping_charge = models.IntegerField(default=99, null=False, blank=False)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    title = models.CharField(blank=False, null=False, unique=True, max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=False, null=False)
    discount_price = models.DecimalField(max_digits=10, decimal_places=0)
    # image_list = models.CharField # Make one-to-many relationship
    total_stock = models.DecimalField(max_digits=10, decimal_places=0)
    description = models.TextField()
    category = TreeForeignKey(
        Category, related_name="product_category", on_delete=models.SET_NULL, null=True, blank=True
    )
    image1 = models.CharField(max_length=100, blank=True, null=True)
    image2 = models.CharField(max_length=100, blank=True, null=True)
    image3 = models.CharField(max_length=100, blank=True, null=True)
    image4 = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


# class Image

class DeliveryPlace(models.Model):
    price = models.IntegerField(blank=False, null=False, default=500)
    # category = models.ForeignKey(Category, related_name="category_charge", on_delete=models.CASCADE)
    place = models.CharField(blank=False, null=False, unique=True, max_length=100)

    def __str__(self) -> str:
        return self.place
