from rest_framework import serializers

from core.settings import LANGUAGES, LANGUAGES_FLAGS
from .models import *


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

# Добавляем is_premium в Category
    def to_representation(self, instance):
        representation = super(CategorySerializer, self).to_representation(instance)
        if self.context.get('request').user.is_authenticated:
            representation['is_premium'] = self.context.get('request').user.is_premium()
        return representation


class DescriptionInlineSerializer(serializers.ModelSerializer):
    favorite = serializers.BooleanField(default=True)

    class Meta:
        model = Description
        fields = ('id', 'image', 'title', 'favorite')


class DescriptionSerializer(serializers.ModelSerializer):
    favorite = serializers.BooleanField(read_only=True, default=False)

    class Meta:
        model = Description
        fields = ('id', 'image', 'favorite')

# Фильрация по languages
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
            a[f'audio_file_{language}'] = self.context.get('request').build_absolute_uri(getattr(instance, f'audio_file_{language}').url) if getattr(instance, f'audio_file_{language}') else None
            languages_list.append(a)
        representation['languages'] = languages_list
        return representation


class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = ('id', 'favorite', 'description')

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        description = validated_data.get('description')
        favorite = Favorite.objects.filter(user=user, description=description).first()
        if favorite:
            favorite.delete()
        else:
            return Favorite.objects.get_or_create(user=user, description=description, favorite=True)[0]
        return favorite


class DescriptionFavoritesSerializer(DescriptionSerializer):
    favorite = serializers.BooleanField(default=True)
