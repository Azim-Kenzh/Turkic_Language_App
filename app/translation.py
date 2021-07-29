from modeltranslation.translator import translator, TranslationOptions
from .models import *


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', )


class DescriptionTranslationOptions(TranslationOptions):
    fields = ('title', 'audio_file')


translator.register(Category, CategoryTranslationOptions)
translator.register(Description, DescriptionTranslationOptions)
