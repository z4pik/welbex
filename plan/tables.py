import django_tables2 as tables
from .models import Plan


class PlanTable(tables.Table):
    class Meta:
        model = Plan
