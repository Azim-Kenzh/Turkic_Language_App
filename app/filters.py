from django_filters import FilterSet
from django_filters import rest_framework as filters

from .models import Description, Favorite


class DescriptionFilter(FilterSet):
    category = filters.CharFilter('category')

    class Meta:
        models = Description
        fields = ('category', )


# class FavoriteFilter(FilterSet):
#     description , category = filters.CharFilter('category')
#
#     class Meta:
#         models = Description
#         fields = ('category',)


