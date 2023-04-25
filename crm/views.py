from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, UpdateView, DeleteView

from .forms import TaskForm
from .models import Task, Project, Employee
from .utils import do_dict, TestIsAuthorThisTask


class MainView(LoginRequiredMixin, TemplateView):
    template_name = 'kanban_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = Task

        context['todo'] = do_dict(task.objects.filter(status='TD').order_by('end', 'priority'))
        context['doing'] = do_dict(task.objects.filter(status='DO').order_by('end', 'priority'))
        context['done'] = do_dict(task.objects.filter(status='DN').order_by('end', 'priority'))
        context['release'] = do_dict(task.objects.filter(status='RL').order_by('end', 'priority'))
        return context


class ProjectView(LoginRequiredMixin, TemplateView):
    template_name = 'kanban_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = Task
        project = get_object_or_404(Project, id=self.kwargs['pk'])

        context['todo'] = do_dict(task.objects.filter(status='TD', project=project).order_by('end', 'priority'))
        context['doing'] = do_dict(task.objects.filter(status='DO', project=project).order_by('end', 'priority'))
        context['done'] = do_dict(task.objects.filter(status='DN', project=project).order_by('end', 'priority'))
        context['release'] = do_dict(task.objects.filter(status='RL', project=project).order_by('end', 'priority'))
        context['projectname'] = project
        return context


class EmployeeView(LoginRequiredMixin, TemplateView):
    template_name = 'kanban_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = Task
        employee = get_object_or_404(Employee, id=self.kwargs['pk'])

        context['todo'] = do_dict(task.objects.filter(status='TD', employee=employee).order_by('end', 'priority'))
        context['doing'] = do_dict(task.objects.filter(status='DO', employee=employee).order_by('end', 'priority'))
        context['done'] = do_dict(task.objects.filter(status='DN', employee=employee).order_by('end', 'priority'))
        context['release'] = do_dict(task.objects.filter(status='RL', employee=employee).order_by('end', 'priority'))
        context['employeename'] = employee
        return context


class TaskUpdate(LoginRequiredMixin, TestIsAuthorThisTask, UpdateView):
    form_class = TaskForm
    model = Task
    template_name = 'task_edit.html'
    reverse_lazy('kanban_page')


class TaskDelete(LoginRequiredMixin, TestIsAuthorThisTask, DeleteView):
    model = Task
    success_url = reverse_lazy('kanban_page')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
