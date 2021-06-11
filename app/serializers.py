from rest_framework import serializers

from .models import *


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ('title', 'title_ru')


class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Word
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = instance.category.title
        return representation


class DescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Description
        exclude = ('title', 'title_ru', 'audio_file', 'audio_file_ru')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['word'] = instance.word.title
        return representation


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('word', 'user', 'favorite')

    def get_fields(self):
        action = self.context.get('action')
        fields = super().get_fields()
        if action == 'create':
            fields.pop('user')
            fields.pop('favorite')
        return fields

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.user.username
        representation['word'] = instance.word.title
        return representation

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        word = validated_data.get('word')
        favorite = Favorite.objects.get_or_create(user=user, word=word)[0]
        favorite.favorite = True if favorite.favorite == False else False
        favorite.save()
        return favorite