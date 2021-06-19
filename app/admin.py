from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin
from .models import *

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    exclude = ('title_ru', )
    list_display = ('id', 'title')
    list_filter = ('title', )


@admin.register(Description)
class DescriptionAdmin(TranslationAdmin):
    exclude = ('title_ru', 'audio_file_ru', 'images_ru')
    list_display = ('id', 'title', 'audio_file')
    list_filter = ('title', )


admin.site.register(Favorite)


