from rest_framework import generics
from .permissions import IsAdminOrReadOnly
from .serializers import *
from .models import *


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
