from .models import Plan
import django_filters
from django_filters import filters


class PlanFilter(django_filters.FilterSet):
    quantity = filters.RangeFilter()
    distance = filters.RangeFilter()

    class Meta:
        model = Plan
        fields = ['title']
