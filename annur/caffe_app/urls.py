from django.urls import path, include
from rest_framework import routers
from .views import *



routers =routers.SimpleRouter()

urlpatterns = [
    path('', include(routers.urls)),
    # UserProfile
    path('users/', UserProfileListAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),

    # Restoran
    path('caffe/', RestoranListAPIView.as_view(), name='caffe_list'),
    path('caffe/<int:pk>/', RestoranRetrieveAPIView.as_view(), name='caffe_detail'),
    path('caffe/create/', RestoranCreateAPIView.as_view(), name='caffe_create'),

    # Category
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('category_create/', CategoryCreateAPIView.as_view(), name='category_create'),
    path('category/<int:pk>/edit/', CategoryRetrieveAPIView.as_view(), name='category_edit'),

    # Subcategory
    path('subcategory/', SubCategoryListAPIView.as_view(), name='subcategory_list'),
    path('subcategory/<int:pk>/', SubCategoryDetailAPIView.as_view(), name='subcategory_detail'),
    path('subcategory_create/', SubCategoryCreateAPIView.as_view(), name='subcategory_create'),
    path('subcategory/<int:pk>/edit/', SubCategoryRetrieveAPIView.as_view(), name='subcategory_edit'),

    # Product
    path('product/', ProductListAPIView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
    path('product_create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('product/<int:pk>/edit/', ProductRetrieveAPIView.as_view(), name='product_edit'),

    # ProductImage
    path('product_image/', ProductImageListAPIView.as_view(), name='product_image_list'),
    path('product_image/<int:pk>/', ProductImageDetailAPIView.as_view(), name='product_image_detail'),
    path('product_image_create/', ProductImageCreateAPIView.as_view(), name='product_image_create'),
    path('product_image/<int:pk>/edit/', ProductImageRetrieveAPIView.as_view(), name='product_image_edit'),

    # CafeImage
    path('cafe_image/', CafeImageListAPIView.as_view(), name='cafe_image_list'),
    path('cafe_image/<int:pk>/', CafeImageDetailAPIView.as_view(), name='cafe_image_detail'),
    path('cafe_image_create/', CafeImageCreateAPIView.as_view(), name='cafe_image_create'),
    path('cafe_image/<int:pk>/edit/', CafeImageRetrieveAPIView.as_view(), name='cafe_image_edit'),

    # AboutUs
    path('about/', AboutUsListAPIView.as_view(), name='about_list'),
    path('about/<int:pk>/', AboutUsDetailAPIView.as_view(), name='about_detail'),
    path('about_create/', AboutUsCreateAPIView.as_view(), name='about_create'),
    path('about/<int:pk>/edit/', AboutUsRetrieveAPIView.as_view(), name='about_edit'),

    # OpeningHours
    path('opening_hours/', OpeningHoursListAPIView.as_view(), name='opening_hours_list'),
    path('opening_hours/<int:pk>/', OpeningHoursDetailAPIView.as_view(), name='opening_hours_detail'),
    path('opening_hours_create/', OpeningHoursCreateAPIView.as_view(), name='opening_hours_create'),
    path('opening_hours/<int:pk>/edit/', OpeningHoursRetrieveAPIView.as_view(), name='opening_hours_edit'),

    # Contact
    path('contact/', ContactListAPIView.as_view(), name='contact_list'),
    path('contact/<int:pk>/', ContactDetailAPIView.as_view(), name='contact_detail'),
    path('contact_create/', ContactCreateAPIView.as_view(), name='contact_create'),
    path('contact/<int:pk>/edit/', ContactRetrieveAPIView.as_view(), name='contact_edit'),
]
