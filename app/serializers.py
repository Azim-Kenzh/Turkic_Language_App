from rest_framework import serializers

from core.settings import LANGUAGES, LANGUAGES_FLAGS
from .models import *


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = ('image',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = instance.category.title
        languages_list = []
        for language in LANGUAGES:
            language = language[0]
            a = {}
            a[f'title_{language}'] = getattr(instance, f'title_{language}')
            a[f'image_{language}'] = self.context.get('request').build_absolute_uri(LANGUAGES_FLAGS.get(language)[1])
            a[f'language_{language}'] = LANGUAGES_FLAGS.get(language)[0]
            a[f'audio_file_{language}'] =self.context.get('request').build_absolute_uri(getattr(instance, f'audio_file_{language}').url) if getattr(instance, f'audio_file_{language}') else None
            languages_list.append(a)
            # representation[language] = a
        representation['languages'] = languages_list
        return representation


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('description', 'id')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.user.username
        representation['description'] = instance.description.title
        return representation

