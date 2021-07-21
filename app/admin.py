from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin, TranslationInlineModelAdmin
from .models import *

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    exclude = ('title_ru', )
    list_display = ('id', 'title', 'is_free')
    search_fields = ('title',)
    ordering = ('title',)



@admin.register(Description)
class DescriptionAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'audio_file')
    search_fields = ('title', )
    ordering = ('title', )

    fields = ['image', 'category',
              ('title_tr', 'audio_file_tr'),
              ('title_az', 'audio_file_az'),
              ('title_uz', 'audio_file_uz'),
              ('title_kk', 'audio_file_kk'),
              ('title_ug', 'audio_file_ug'),
              ('title_tk', 'audio_file_tk'),
              ('title_tt', 'audio_file_tt'),
              ('title_ky', 'audio_file_ky'),
              ('title_ksk', 'audio_file_ksk'),
              ('title_ba', 'audio_file_ba'),
              ('title_cv', 'audio_file_cv'),
              ('title_ash', 'audio_file_ash'),
              ('title_kaa', 'audio_file_kaa'),
              ('title_krc', 'audio_file_krc'),
              ('title_sah', 'audio_file_sah'),
              ('title_crh', 'audio_file_crh'),
              ('title_alt', 'audio_file_alt'),
            ]


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'description')




