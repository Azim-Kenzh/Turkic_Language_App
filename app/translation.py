
from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'slug')
    # empty_values = {'slug': None}


@register(Word)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(Description)
class DescriptionTranslationOptions(TranslationOptions):
    fields = ('description', )