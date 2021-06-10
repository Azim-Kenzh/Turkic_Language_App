from django_filters import FilterSet
from django_filters import rest_framework as filters

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
