from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name', 'description')



@register(Restoran)
class RestoranTranslationOptions(TranslationOptions):
    fields = ('names', 'description')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name', 'description')


@register(Subcategory)
class SubcategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('information', 'description')

@register(OpeningHours)
class OpeningHoursTranslationOptions(TranslationOptions):
    fields = ('description',)
