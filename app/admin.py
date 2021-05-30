from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin
from .models import *

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('title', 'slug')


@admin.register(Word)
class ProductAdmin(TranslationAdmin):
    list_display = ('title', )


@admin.register(Description)
class DescriptionAdmin(TranslationAdmin):
    list_display = ('title', 'audio_file')


admin.site.register(Favorite)


