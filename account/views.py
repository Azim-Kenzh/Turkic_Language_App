from rest_framework import status, mixins, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from account import models, serializers
from account.models import MyUser
from account.serializers import RegisterSerializer, UserSerializer



class RegisterView(APIView):

    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Вы успешно зарегистрировались!', status=status.HTTP_201_CREATED)


class LoginView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'email': user.email,
        })



    # def post(self, request):
    #     serializer = serializers.LoginSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     username = serializer.validated_data['username']
    #     info = models.User.objects.get(username=username)
    #     serializer1 = serializers.UserSerializer(info, many=True)
    #     token, created = Token.objects.get_or_create(username=username)
    #     return Response({"token": token.key, 'data': serializer1.data}, status=200)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('успешно вышли из системы', status=status.HTTP_200_OK)

#
class UserViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'email'
    lookup_url_kwarg = 'email'
    lookup_value_regex = '[\w@.]+'

    def get_permissions(self):
        if self.action in ['retrieve', 'partial_update', 'destroy', 'update']:
            permissions = [IsAuthenticated, ]
        else:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def get_serializer_context(self):
        return {'request': self.request, 'action': self.action}