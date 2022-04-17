from django.shortcuts import render, redirect
from .filters import PlanFilter
from django.views.generic import TemplateView, ListView
from .forms import PlanCreateForm
from .models import Plan
from django.core.paginator import Paginator


# Create your views here.


def index(request):
    plan_list = Plan.objects.all()
    myFilter = PlanFilter(request.GET, queryset=plan_list)  # Фильтрация
    plan_list = myFilter.qs
    p = Paginator(plan_list, 5)  # Пагинация по 5 записей на страницу
    page = request.GET.get('page')
    plans = p.get_page(page)
    form = PlanCreateForm(request.POST or None, files=request.FILES or None) # Форма добавления новой записи
    if request.method == 'POST':
        form = PlanCreateForm(request.POST, request.FILES)
        if form.is_valid():
            Plan.objects.create(**form.cleaned_data)
            return redirect('index')
        return render(request, {'form': form})
    form = PlanCreateForm()
    return render(
        request, 'plan/index.html', {
            'plan_list': plan_list,
            'plans': plans,
            'myFilter': myFilter,
            'form': form,
        }
    )

