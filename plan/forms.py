from django import forms
from .models import Plan


class PlanCreateForm(forms.ModelForm):
    """Форма создания нового поста"""
    class Meta:
        model = Plan
        fields = ['title', 'quantity', 'distance']