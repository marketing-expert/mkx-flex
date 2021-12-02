# max.filters.py

import django_filters
from max import models


class MaxFilter(django_filters.FilterSet):

    number_kit = django_filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = models.Souscriber
        fields = ['number_kit', 'phone_one']