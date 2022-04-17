from django import forms
from .models import Plan


class PlanCreateForm(forms.ModelForm):
    """"""
    class Meta:
        model = Plan
        fields = ['title', 'quantity', 'distance']