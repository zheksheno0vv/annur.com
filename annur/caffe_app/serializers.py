from .models import *
from rest_framework import serializers


class UserListSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class RestoranListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Restoran
        fields = ['id', 'names', 'description', 'age_work', 'dishes', 'link', 'rating']


class RestoranDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Restoran
        fields = ['id', 'names', 'description', 'age_work', 'dishes', 'link', 'rating']


class CategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'description', 'category_icon']


class SubCategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'description', 'subimage']


class CategoryDetailSerializers(serializers.ModelSerializer):
    subcategories = SubCategoryListSerializers(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'category_name', 'description', 'category_icon', 'subcategories']


class ProductImageListSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductImageDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'price', 'gram', 'sub_category']


class ProductDetailSerializers(serializers.ModelSerializer):
    images = ProductImageListSerializers(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'description', 'price', 'gram', 'sub_category', 'images']


class SubCategoryDetailSerializers(serializers.ModelSerializer):
    products = ProductListSerializers(many=True, read_only=True)

    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'description', 'subimage', 'products']


class CafeImageListSerializers(serializers.ModelSerializer):
    class Meta:
        model = CafeImage
        fields = '__all__'


class CafeImageDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = CafeImage
        fields = '__all__'


class AboutUsListSerializers(serializers.ModelSerializer):
    cafe_images = CafeImageListSerializers(many=True, read_only=True)

    class Meta:
        model = AboutUs
        fields = ['id', 'information', 'description', 'cafe_images']


class AboutUsDetailSerializers(serializers.ModelSerializer):
    cafe_images = CafeImageListSerializers(many=True, read_only=True)

    class Meta:
        model = AboutUs
        fields = ['id', 'information', 'description', 'image_admin', 'cafe_images']


class OpeningHoursListSerializers(serializers.ModelSerializer):
    class Meta:
        model = OpeningHours
        fields = ['id', 'data', 'work_day', 'description']


class OpeningHoursDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = OpeningHours
        fields = ['id', 'data', 'work_day', 'description']


class ContactListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'whatsup', 'phone_cafe', 'admin_phone', 'insta_urls']


class ContactDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'whatsup', 'phone_cafe', 'admin_phone', 'insta_urls']
