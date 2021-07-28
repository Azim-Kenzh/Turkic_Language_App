import django.contrib.auth.password_validation as validators
from rest_framework import serializers

from account.models import *
from app.models import Favorite


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True, style={'input_type': 'password'})
    password_confirm = serializers.CharField(min_length=6, write_only=True, style={'input_type': 'password'})

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password', 'password_confirm')

    def validate_username(self, username):
        if MyUser.objects.filter(username=username).exists():
            raise serializers.ValidationError('Есть пользователь с таким именем')
        return username

    def validate(self, validate_data): # def validate - def clean, validate_data - clean_data
        password = validate_data.get('password')
        password_confirm = validate_data.get('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('password do not match')
        return validate_data

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = MyUser.objects.create_user(username=username, email=email, password=password)
        return user


class UserSerializer(serializers.ModelSerializer):
    favorite_words = serializers.IntegerField(read_only=True)
    is_premium = serializers.BooleanField()

    class Meta:
        model = MyUser
        fields = ('id', 'image', 'username', 'email', 'favorite_words', 'is_premium')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context['request'].user.is_premium():
            representation['favorite_words'] = instance.favorites.count()
        return representation

    # def update(self, instance, validated_data):
    #     instance.username = validated_data.get('username', instance.username,)
    #     print('instance of username', instance.username)
    #     return instance


class UserUpdateSerializer(serializers.ModelSerializer):
    # favorites = FavoriteSerializer(many=True)

    class Meta:
        model = MyUser
        fields = ('image', 'username')




# class UserResetPasswordSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(source='user.password',  max_length=20, min_length=6)
#     new_password = serializers.CharField(style={'input_type': 'password'}, max_length=20, min_length=)
#     class Meta:
#         model = MyUser
#         fields =("password", 'new_password')

