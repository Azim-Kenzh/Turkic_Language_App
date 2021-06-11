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
    category = filters.CharFilter('category')

    class Meta:
        models = Description
        fields = ('category', )
