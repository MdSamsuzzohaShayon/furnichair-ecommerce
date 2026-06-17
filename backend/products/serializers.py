from rest_framework import serializers
from .models import Product, Category, DeliveryPlace


# class AccountSerializer(serializers.ModelSerializer):
#     url = serializers.CharField(source='get_absolute_url', read_only=True)

#     class Meta:
#         model = Account


class ProductUpdateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(read_only=True)
    discount_price = serializers.DecimalField(max_digits=10, decimal_places=0, required=False)
    total_stock = serializers.DecimalField(max_digits=10, decimal_places=0, required=False)
    description = serializers.CharField(required=False)

    # category = TreeForeignKey(
    #     Category, related_name="product_category", on_delete=models.SET_NULL, null=True, blank=True
    # )
    # image1 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    # image2 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    # image3 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    # image4 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    # discount_price = serializers.SerializerMethodField(required=False)
    # total_stock = serializers.SerializerMethodField(required=False)
    # description = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Product
        fields = "__all__"
        # exclude = ["id"]


class ProductCreateSerializer(serializers.ModelSerializer):
    image1 = serializers.CharField(read_only=True)
    image2 = serializers.CharField(read_only=True)
    image3 = serializers.CharField(read_only=True)
    image4 = serializers.CharField(read_only=True)

    image1file = serializers.ImageField(write_only=True,
                                        required=False)  # We must provide write only in order to pop it
    image2file = serializers.ImageField(write_only=True,
                                        required=False)  # We must provide write only in order to pop it
    image3file = serializers.ImageField(write_only=True,
                                        required=False)  # We must provide write only in order to pop it
    image4file = serializers.ImageField(write_only=True,
                                        required=False)  # We must provide write only in order to pop it

    class Meta:
        model = Product
        fields = "__all__"


class DeliveryPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPlace
        fields = "__all__"


class CategoryCreateSerializer(serializers.ModelSerializer):
    image = serializers.CharField(read_only=True)
    categoryimage = serializers.ImageField(write_only=True)  # We must provide write only in order to pop it

    class Meta:
        model = Category
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)

    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, read_only=True)
    class Meta:
        model = Product
        fields = "__all__"
        # exclude = ["id"]

    # def create(self, validated_data):
    #     images_data = self.context.get('view').request.FILES
    #     images = [Product(image=image_data) for image_data in images_data.values()]
    #     return Product.objects.bulk_create(images)
