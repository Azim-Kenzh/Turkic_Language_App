
from rest_framework import generics, viewsets, mixins, filters
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *
from .filters import WordFilter, DescriptionFilter


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
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ['title', ]


class WordViewSet(PermissionMixin, viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [AllowAny, ]

    """# /api/v1/words/?category = id DjangoFilterBackend"""
    """/api/v1/words/?search= str filters.SearchFilter"""
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = WordFilter
    search_fields = ['title', ]


class DescriptionViewSet(PermissionMixin, viewsets.ModelViewSet):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer
    permission_classes = [AllowAny, ]

    """/ api / v1 / descriptions /?word = 1"""
    filter_backends = (DjangoFilterBackend,)
    filter_class = DescriptionFilter


class FavoriteViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated, ]

    def get_serializer_context(self):
        return {'request': self.request, 'action': self.action}
