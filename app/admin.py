from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin
from .models import *

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'slug')
    list_filter = ('title', )

@admin.register(Word)
class ProductAdmin(TranslationAdmin):
    list_display = ('id', 'title', )
    list_filter = ('title', )

@admin.register(Description)
class DescriptionAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'audio_file')
    list_filter = ('title', )


admin.site.register(Favorite)


