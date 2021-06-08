from django.contrib.auth import authenticate
from rest_framework import serializers

from account.models import *
from app.serializers import FavoriteSerializer


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True)
    # password_confirm = serializers.CharField(min_length=6, write_only=True)

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password')

    def validate_username(self, username):
        if MyUser.objects.filter(username=username).exists():
            raise serializers.ValidationError('Bu isimde bir kullanıcı var')
        return username

    # def validate(self, validate_data): # def validate - def clean, validate_data - clean_data
    #     password = validate_data.get('password')
    #     password_confirm = validate_data.get('password_confirm')
    #     if password != password_confirm:
    #         raise serializers.ValidationError('password do not match')
    #     return validate_data

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = MyUser.objects.create_user(username=username, email=email, password=password)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(
        label='Password',
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    class Meta:
        model = MyUser
        fields = ('username', 'email')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['username'] = instance.username.username
        return representation


    def validate(self, validate_data):
        username = validate_data.get('username')
        password = validate_data.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'), username=username, password=password)
            if not user:
                raise serializers.ValidationError('Kullanıcı kayıt olamaz')
        else:
            raise serializers.ValidationError('"Giriş" ve "şifre" belirtmelisiniz!')

        validate_data['user'] = user
        return validate_data


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('username', 'email')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        action = self.context.get('action')
        if action == 'retrieve':
            representation['favorites'] = FavoriteSerializer(instance.favorites.filter(favorite=True),
                                                             many=True, context=self.context).data
        return representation