from rest_framework import generics, viewsets, mixins, filters, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .filters import DescriptionFilter


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


class DescriptionViewSet(PermissionMixin, viewsets.ModelViewSet):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer
    permission_classes = [AllowAny, ]

    """/ api / v1 / descriptions /?word = 1"""
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = DescriptionFilter
    search_fields = ['title', ]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated, ]

    """/ api / v1 / descriptions /?search = asd.."""
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ['description__title', ]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_context(self):
        return {'request': self.request, 'action': self.action}

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

