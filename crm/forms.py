from django import forms
from .models import Task, Employee


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'name',
            'about',
            'project',
            'employee',
            'status',
            'priority',
            'end',
        ]


class PersonalForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'username',
            'email',
            'last_name',
            'first_name',
            'second_name',
            'department',
            'photo',
        ]
