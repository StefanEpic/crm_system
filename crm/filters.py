from django_filters import FilterSet, ModelChoiceFilter, DateFilter, CharFilter
from django.forms import DateInput
from .models import Department, Employee, Project, Task


class PostsFilter(FilterSet):
    title = CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Поиск по задачам'
    )

    project = ModelChoiceFilter(
        field_name='project',
        queryset=Project.objects.all(),
        label='Проекты',
        empty_label='Все'
    )

    employee = ModelChoiceFilter(
        field_name='employee',
        queryset=Employee.objects.all(),
        label='Исполнитель',
        empty_label='Все'
    )

    department = ModelChoiceFilter(
        field_name='department',
        queryset=Department.objects.all(),
        label='Отдел',
        empty_label='Все'
    )

    date = DateFilter(
        field_name='date_in',
        widget=DateInput(attrs={'type': 'date'}),
        label='Дата, от',
        lookup_expr='date__gt'
    )