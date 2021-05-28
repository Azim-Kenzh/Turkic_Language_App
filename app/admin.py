from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin
from .models import *

@admin.register(Category)
class CategoryAdmin(TabbedTranslationAdmin,):
    list_display = ('title', 'slug')


@admin.register(Word)
class ProductAdmin(TabbedTranslationAdmin):
    list_display = ('title', )


@admin.register(Description)
class DescriptionAdmin(TabbedTranslationAdmin):
    list_display = ('description', 'audio_file')


admin.site.register(Favorite)


