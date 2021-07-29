from rest_framework import serializers

from account.models import *


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


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('image', 'username')


