from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken  # Класс для создания access и refresh токенов
from django.contrib.auth import authenticate  # Функция, которая проверяет логин и пароль


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email','first_name', 'last_name',
                  'phone_number')  # Указываем, какие поля включить
        extra_kwargs = {
            'password': {'write_only': True}}  # Пароль не должен отображаться при выводе данных (пороль не будет видно)

    def create(self, validated_data):  # create авоматически хеширует пороль
        user = UserProfile.objects.create_user(**validated_data)  # Используем встроенный метод для создания пользователя
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()  # Поле для логина
    password = serializers.CharField(write_only=True)  # Пароль — только на запись (чыгарып бербейт поролду кайра)

    def validate(self, data):
        user = authenticate(**data)  # Проверка логина и пароля
        if user and user.is_active:  # Если пользователь найден и активен
            return user  # Возвращаем объект пользователя
        raise serializers.ValidationError('Неверные учетные данные')  # Ошибка при неверном логине/пароле

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)  # Создаём refresh токен
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),  # access токен — для авторизации
            'refresh': str(refresh),  # refresh токен — для обновления access токена
        }

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        token = attrs.get('refresh')
        try:
            RefreshToken(token)
        except Exception:
            raise serializers.ValidationError({"refresh": "Невалидный токен"})
        return attrs


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
    images = ProductImageListSerializers(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'price', 'gram', 'sub_category', 'images']


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
