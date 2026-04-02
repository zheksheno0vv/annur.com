from rest_framework import generics, status
from .permissions import IsAdminOrReadOnly
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


# 🔐 РЕГИСТРАЦИЯ ПОЛЬЗОВАТЕЛЯ
class RegisterView(generics.CreateAPIView):
    serializer_class = UserProfileSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)   # Получаем сериализатор с входными данными
        serializer.is_valid(raise_exception=True)                    # Проверяет ошибку если не правильно
        user = serializer.save()                                                          # Сохраняем пользователя (должен быть вызов create_user внутри сериализатора!)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 🔐 КАСТОМНЫЙ ЛОГИН С JWT
class CustomLoginView(TokenObtainPairView):             # Наследование TokenObtainPairView алып атат
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)   # Получаем сериализатор с логин-данными
        try:
            serializer.is_valid(raise_exception=True)                # Пробуем валидировать
        except Exception:
            return Response({'detail': 'Неверные учетные данные'}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data  # Здесь — уже валидные данные и токены
        return Response(serializer.data, status=status.HTTP_200_OK)

        # 🔐 ВЫХОД ИЗ СИСТЕМЫ (ОТЗЫВ refresh-токена)

class LogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            refresh_token = serializer.validated_data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response({'detail': 'Невалидный токен'}, status=status.HTTP_400_BAD_REQUEST)

class UserProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserListSerializers


class UserProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserDetailSerializers


class RestoranListAPIView(generics.ListAPIView):
    queryset = Restoran.objects.all()
    serializer_class = RestoranListSerializers


class RestoranRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Restoran.objects.all()
    serializer_class = RestoranDetailSerializers


class RestoranCreateAPIView(generics.CreateAPIView):
    queryset = Restoran.objects.all()
    serializer_class = RestoranListSerializers
    permission_classes = [IsAdminOrReadOnly]


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializers


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializers


class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializers
    permission_classes = [IsAdminOrReadOnly]


class CategoryRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializers
    permission_classes = [IsAdminOrReadOnly]


class SubCategoryListAPIView(generics.ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubCategoryListSerializers


class SubCategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubCategoryDetailSerializers


class SubCategoryCreateAPIView(generics.CreateAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubCategoryListSerializers
    permission_classes = [IsAdminOrReadOnly]


class SubCategoryRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubCategoryDetailSerializers
    permission_classes = [IsAdminOrReadOnly]


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializers


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializers


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializers
    permission_classes = [IsAdminOrReadOnly]


class ProductRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializers
    permission_classes = [IsAdminOrReadOnly]


class ProductImageListAPIView(generics.ListAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageListSerializers


class ProductImageDetailAPIView(generics.RetrieveAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageDetailSerializers


class ProductImageCreateAPIView(generics.CreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageListSerializers
    permission_classes = [IsAdminOrReadOnly]


class ProductImageRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageDetailSerializers
    permission_classes = [IsAdminOrReadOnly]


class CafeImageListAPIView(generics.ListAPIView):
    queryset = CafeImage.objects.all()
    serializer_class = CafeImageListSerializers


class CafeImageDetailAPIView(generics.RetrieveAPIView):
    queryset = CafeImage.objects.all()
    serializer_class = CafeImageDetailSerializers



class CafeImageCreateAPIView(generics.CreateAPIView):
    queryset = CafeImage.objects.all()
    serializer_class = CafeImageListSerializers
    permission_classes = [IsAdminOrReadOnly]


class CafeImageRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CafeImage.objects.all()
    serializer_class = CafeImageDetailSerializers
    permission_classes = [IsAdminOrReadOnly]


class AboutUsListAPIView(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsListSerializers


class AboutUsDetailAPIView(generics.RetrieveAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsDetailSerializers


class AboutUsCreateAPIView(generics.CreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsListSerializers
    permission_classes = [IsAdminOrReadOnly]


class AboutUsRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsDetailSerializers
    permission_classes = [IsAdminOrReadOnly]


class OpeningHoursListAPIView(generics.ListAPIView):
    queryset = OpeningHours.objects.all()
    serializer_class = OpeningHoursListSerializers


class OpeningHoursDetailAPIView(generics.RetrieveAPIView):
    queryset = OpeningHours.objects.all()
    serializer_class = OpeningHoursDetailSerializers


class OpeningHoursCreateAPIView(generics.CreateAPIView):
    queryset = OpeningHours.objects.all()
    serializer_class = OpeningHoursListSerializers
    permission_classes = [IsAdminOrReadOnly]


class OpeningHoursRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OpeningHours.objects.all()
    serializer_class = OpeningHoursDetailSerializers
    permission_classes = [IsAdminOrReadOnly]


class ContactListAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializers


class ContactDetailAPIView(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactDetailSerializers


class ContactCreateAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializers
    permission_classes = [IsAdminOrReadOnly]


class ContactRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactDetailSerializers
    permission_classes = [IsAdminOrReadOnly]
