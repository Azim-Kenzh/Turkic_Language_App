from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer

from account.models import *
from app.serializers import FavoriteSerializer


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True)
    password_confirm = serializers.CharField(min_length=6, write_only=True)

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
    favorites = FavoriteSerializer(many=True)

    class Meta:
        model = MyUser
        fields = ('id', 'image', 'username', 'email', 'favorites')



