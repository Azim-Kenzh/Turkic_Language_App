
from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', )

@register(Description)
class DescriptionTranslationOptions(TranslationOptions):
    fields = ('title', 'audio_file')