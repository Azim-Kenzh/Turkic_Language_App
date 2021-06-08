from django_filters.rest_framework import DjangoFilterBackend, filters
from django_filters import FilterSet
# from rest_framework import filters

from .models import Word, Description


class WordFilter(FilterSet):
    """Filter for an category"""
    category = filters.CharFilter('category')

    class Meta:
        models = Word
        fields = ('category', )


class DescriptionFilter(FilterSet):
    word = filters.CharFilter('word')

    class Meta:
        models = Description
        fields = ('word', )
