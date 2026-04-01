from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField


class UserProfile(models.Model):
    username = models.CharField(max_length=127, null=True, blank=True)
    last_name = models.CharField(max_length=127, null=True, blank=True)
    first_name = models.CharField(max_length=127, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)
    ROLE_CHOICES = (
        ('admin', 'admin'),
        ('client', 'client')
    )
    user_role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')
    profile_image = models.ImageField(upload_to='profile_image/', null=True, blank=True)

    def __str__(self):
        return f'{self.username}, {self.user_role}'


class Restoran(models.Model):
    names = models.CharField(max_length=150)
    description = models.TextField()
    age_work = models.PositiveSmallIntegerField()
    dishes = models.PositiveSmallIntegerField()
    link = models.URLField(blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = "Ресторан"


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField()
    category_icon = models.ImageField(upload_to='category_icon/')

    def __str__(self):
        return self.category_name


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=100)
    description = models.TextField()
    subimage = models.ImageField(upload_to='sub_images/')

    def __str__(self):
        return self.name


class Product(models.Model):
    sub_category = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='products')
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveSmallIntegerField()
    gram = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.product_name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    product_image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f'{self.product_image}'


class AboutUs(models.Model):
    information = models.TextField()
    description = models.TextField()
    image_admin = models.ImageField(upload_to='admin_images/')

    def __str__(self):
        return f'{self.description}'


class CafeImage(models.Model):
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name='cafe_images')
    cafe_image = models.ImageField(upload_to='cafe_images/')

    def __str__(self):
        return f'{self.about_us}'


class OpeningHours(models.Model):
    DAY_CHOICES = (
        ('ПН', 'ПН'),
        ('ВТ', 'ВТ'),
        ('СР', 'СР'),
        ('ЧТ', 'ЧТ'),
        ('ПТ', 'ПТ'),
        ('СБ', 'СБ'),
        ('ВС', 'ВС'),
    )
    work_day = MultiSelectField(choices=DAY_CHOICES, max_choices=7)
    data = models.DateField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.description}'


class Contact(models.Model):
    whatsup = models.URLField(blank=True)
    phone_cafe = PhoneNumberField(region='KG')
    admin_phone = PhoneNumberField(region='KG')
    insta_urls = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.phone_cafe}'
