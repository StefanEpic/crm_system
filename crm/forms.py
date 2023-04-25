from django import forms
from .models import Task


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

