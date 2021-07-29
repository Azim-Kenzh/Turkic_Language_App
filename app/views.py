from itertools import groupby
from django.db.models import Exists, OuterRef
from rest_framework import generics, viewsets, filters, status
from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import AllowAny, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .permissions import PaymentPermission
from .serializers import *
from .filters import DescriptionFilter


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all().order_by('-is_free')
    serializer_class = CategorySerializer
    permission_classes = [AllowAny, ]
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ['title', ]


class DescriptionViewSet(viewsets.ModelViewSet):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer
    permission_classes = [PaymentPermission, ]

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
        if self.request.user.is_authenticated:
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
            new_data.append({'category_id': k[0], 'category_title': k[1], 'words': DescriptionInlineSerializer(list(map(lambda x: x.description, v)), many=True, context={'request': request}).data})
        return Response(new_data)


"""Вывод """
@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def description_detail_favorites(request, pk):
    try:
        snippet = Category.objects.get(pk=pk)
    except Description.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    favorite = Favorite.objects.filter(user=request.user, description__category_id=pk)
    serializer = DescriptionFavoritesSerializer(list(map(lambda x: x.description, favorite)), many=True, context={'request': request})
    return Response(serializer.data)


