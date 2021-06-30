from itertools import groupby
from pprint import pprint

from django.db.models import Exists, OuterRef, Q
from rest_framework import generics, viewsets, mixins, filters, status
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from social_core.pipeline import user

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

    """/ api / v1 / descriptions /?category = 1"""
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = DescriptionFilter
    search_fields = ['title', ]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def get_queryset(self):
        queryset = self.filter_queryset(self.queryset)
        favorites = Favorite.objects.select_related('user', 'description').\
            filter(user=self.request.user, description_id=OuterRef('pk'))
        queryset = queryset.annotate(favorite=Exists(favorites))
        return queryset


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated, ]

    """/ api / v1 / descriptions /?search = asd.."""
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ['description__title', 'description__category']


    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_context(self):
        return {'request': self.request, 'action': self.action}

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        search = request.query_params.get('search')
        queryset = self.get_queryset().select_related('description', 'description__category')
        if search:
            queryset = queryset.filter(description__title__icontains=search)
        queryset = list(queryset)
        grouped_iterator = groupby(queryset, lambda x: (x.description.category_id, x.description.category.title))
        data = {}

        for k, v in grouped_iterator:
            if data.get(k, None):
                data[k].append(*list(v))
            else:
                data[k] = list(v)
        new_data = []
        for k, v in data.items():
            new_data.append({'category_id': k[0], 'category_title': k[1], 'words': DescriptionInlineSerializer(list(map(lambda x: x.description, v)), many=True).data})
        return Response(new_data)


    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.description.category.titl
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)


"""Вывод """
@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def description_detail(request, pk):

    try:
        snippet = Category.objects.get(pk=pk)
    except Description.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    favorite = Favorite.objects.filter(user=request.user, description__category_id=pk)
    serializer = DescriptionFavoritesSerializer(list(map(lambda x: x.description, favorite)), many=True, context={'request': request})
    return Response(serializer.data)


