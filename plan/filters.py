from .models import Plan
import django_filters
from django_filters import filters


class PlanFilter(django_filters.FilterSet):
    """
        Поиск по названию + фильтрация по количеству и расстоянию
    """
    quantity = filters.RangeFilter()
    distance = filters.RangeFilter()

    class Meta:
        model = Plan
        fields = ['title']
