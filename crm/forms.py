from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

from .models import Task, Employee


class TaskForm(forms.ModelForm):
    employee = forms.ModelMultipleChoiceField(queryset=Employee.objects.exclude(id=1))

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


class ProfileForm(forms.ModelForm):
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


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Employee
        fields = ['username', 'email', 'password1', 'password2']
