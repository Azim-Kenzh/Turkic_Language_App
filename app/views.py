from django.db.models import Q
from rest_framework import generics, viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .serializers import *


class PermissionMixin:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsAdminUser, ]
        elif self.action in ['update', 'partial_update', 'delete']:
            permissions = [IsAdminUser, ]
        elif self.action == 'get':
            permissions = [AllowAny, ]
        else:
            permissions = []
        return [perm() for perm in permissions]

    def get_serializer_context(self):
        return {'request': self.request, 'action': self.action}


class CategoryListView(generics.ListAPIView, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny, ]


class WordViewSet(PermissionMixin, viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [AllowAny, ]

    """Поиск"""
    @action(detail=False, methods=['get'])
    def search(self, request, pk=None):
        q = request.query_params.get('q')
        queryset = self.get_queryset()
        queryset = queryset.filter(Q(title__icontains=q))
        serializer = WordSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class DescriptionViewSet(PermissionMixin, viewsets.ModelViewSet):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer
    permission_classes = [AllowAny, ]



class FavoriteViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated, ]

    def get_serializer_context(self):
        return {'request': self.request, 'action': self.action}
