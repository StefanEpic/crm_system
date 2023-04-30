from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView

from .forms import TaskForm, ProfileForm
from .models import Task, Project, Employee, Department
from .utils import do_dict, TestIsAuthorThisTask


class KanbanView(LoginRequiredMixin, TemplateView):
    template_name = 'kanban_page.html'
    form_class = TaskForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        task = Task
        todo = do_dict(task.objects.filter(status='TD').order_by('end', 'priority'))
        doing = do_dict(task.objects.filter(status='DO').order_by('end', 'priority'))
        done = do_dict(task.objects.filter(status='DN').order_by('end', 'priority'))
        release = do_dict(task.objects.filter(status='RL').order_by('end', 'priority'))

        columns = (
            {'label': 'Запланировано', 'tag': 'todo', 'objects': todo},
            {'label': 'В работе', 'tag': 'doing', 'objects': doing},
            {'label': 'На проверке', 'tag': 'done', 'objects': done},
            {'label': 'Завершено', 'tag': 'release', 'objects': release}
        )

        context['columns'] = columns
        context['user_pk'] = self.request.user.pk
        context['is_manager'] = self.request.user.groups.filter(name='Управление').exists()
        context['projects'] = Project.objects.all()
        context['employees'] = Employee.objects.exclude(id=1)
        context['departments'] = Department.objects.all()
        return context


class ProjectView(LoginRequiredMixin, TemplateView):
    template_name = 'kanban_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = Task
        project = get_object_or_404(Project, id=self.kwargs['pk'])

        todo = do_dict(task.objects.filter(status='TD', project=project).distinct().order_by('end', 'priority'))
        doing = do_dict(task.objects.filter(status='DO', project=project).distinct().order_by('end', 'priority'))
        done = do_dict(task.objects.filter(status='DN', project=project).distinct().order_by('end', 'priority'))
        release = do_dict(task.objects.filter(status='RL', project=project).distinct().order_by('end', 'priority'))

        columns = (
            {'label': 'Запланировано', 'tag': 'todo', 'objects': todo},
            {'label': 'В работе', 'tag': 'doing', 'objects': doing},
            {'label': 'На проверке', 'tag': 'done', 'objects': done},
            {'label': 'Завершено', 'tag': 'release', 'objects': release}
        )

        context['columns'] = columns
        context['user_pk'] = self.request.user.pk
        context['is_manager'] = self.request.user.groups.filter(name='Управление').exists()
        context['projects'] = Project.objects.all()
        context['employees'] = Employee.objects.exclude(id=1)
        context['departments'] = Department.objects.all()

        context['page_title'] = project
        return context


class EmployeeView(LoginRequiredMixin, TemplateView):
    template_name = 'kanban_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = Task
        employee = get_object_or_404(Employee, id=self.kwargs['pk'])

        todo = do_dict(task.objects.filter(status='TD', employee=employee).distinct().order_by('end', 'priority'))
        doing = do_dict(task.objects.filter(status='DO', employee=employee).distinct().order_by('end', 'priority'))
        done = do_dict(task.objects.filter(status='DN', employee=employee).distinct().order_by('end', 'priority'))
        release = do_dict(task.objects.filter(status='RL', employee=employee).distinct().order_by('end', 'priority'))

        columns = (
            {'label': 'Запланировано', 'tag': 'todo', 'objects': todo},
            {'label': 'В работе', 'tag': 'doing', 'objects': doing},
            {'label': 'На проверке', 'tag': 'done', 'objects': done},
            {'label': 'Завершено', 'tag': 'release', 'objects': release}
        )

        context['columns'] = columns
        context['user_pk'] = self.request.user.pk
        context['is_manager'] = self.request.user.groups.filter(name='Управление').exists()
        context['projects'] = Project.objects.all()
        context['employees'] = Employee.objects.exclude(id=1)
        context['departments'] = Department.objects.all()

        context['page_title'] = employee
        return context


class DepartmentView(LoginRequiredMixin, TemplateView):
    template_name = 'kanban_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = Task
        department = get_object_or_404(Department, id=self.kwargs['pk'])
        employees = set(Employee.objects.filter(department=department))

        todo = do_dict(task.objects.filter(status='TD', employee__in=employees).distinct().order_by('end', 'priority'))
        doing = do_dict(task.objects.filter(status='DO', employee__in=employees).distinct().order_by('end', 'priority'))
        done = do_dict(task.objects.filter(status='DN', employee__in=employees).distinct().order_by('end', 'priority'))
        release = do_dict(
            task.objects.filter(status='RL', employee__in=employees).distinct().order_by('end', 'priority'))

        columns = (
            {'label': 'Запланировано', 'tag': 'todo', 'objects': todo},
            {'label': 'В работе', 'tag': 'doing', 'objects': doing},
            {'label': 'На проверке', 'tag': 'done', 'objects': done},
            {'label': 'Завершено', 'tag': 'release', 'objects': release}
        )

        context['columns'] = columns
        context['user_pk'] = self.request.user.pk
        context['is_manager'] = self.request.user.groups.filter(name='Управление').exists()
        context['projects'] = Project.objects.all()
        context['employees'] = Employee.objects.exclude(id=1)
        context['departments'] = Department.objects.all()

        context['page_title'] = department
        return context


class MyView(LoginRequiredMixin, TemplateView):
    template_name = 'kanban_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = Task
        user = self.request.user

        todo = do_dict(task.objects.filter(status='TD', employee=user.pk).order_by('end', 'priority'))
        doing = do_dict(task.objects.filter(status='DO', employee=user.pk).order_by('end', 'priority'))
        done = do_dict(task.objects.filter(status='DN', employee=user.pk).order_by('end', 'priority'))
        release = do_dict(task.objects.filter(status='RL', employee=user.pk).order_by('end', 'priority'))

        columns = (
            {'label': 'Запланировано', 'tag': 'todo', 'objects': todo},
            {'label': 'В работе', 'tag': 'doing', 'objects': doing},
            {'label': 'На проверке', 'tag': 'done', 'objects': done},
            {'label': 'Завершено', 'tag': 'release', 'objects': release}
        )

        context['columns'] = columns
        context['user_pk'] = self.request.user.pk
        context['projects'] = Project.objects.all()
        context['employees'] = Employee.objects.exclude(id=1)
        context['departments'] = Department.objects.all()

        context['page_title'] = user
        return context


class TaskCreate(CreateView):
    form_class = TaskForm
    model = Task
    template_name = 'task_edit.html'
    success_url = reverse_lazy('kanban_page')

    def form_valid(self, form):
        task = form.save(commit=False)
        task.author_id = int(self.request.user.pk)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_pk'] = self.request.user.pk
        context['projects'] = Project.objects.all()
        context['employees'] = Employee.objects.exclude(id=1)
        context['departments'] = Department.objects.all()
        context['page_title'] = 'Создать'
        return context


class TaskEdit(LoginRequiredMixin, TestIsAuthorThisTask, UpdateView):
    form_class = TaskForm
    model = Task
    template_name = 'task_edit.html'
    success_url = reverse_lazy('kanban_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_pk'] = self.request.user.pk
        context['projects'] = Project.objects.all()
        context['employees'] = Employee.objects.exclude(id=1)
        context['departments'] = Department.objects.all()
        context['page_title'] = 'Редактировать'
        return context


class TaskDelete(LoginRequiredMixin, TestIsAuthorThisTask, DeleteView):
    model = Task
    success_url = reverse_lazy('kanban_page')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class ProfileView(LoginRequiredMixin, UpdateView):
    form_class = ProfileForm
    model = Employee
    template_name = 'profile/profile.html'
    success_url = reverse_lazy('kanban_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['page_title'] = user
        return context


def transfer_to_todo(request, pk):
    task = Task.objects.get(id=pk)
    task.status = 'TD'
    task.save(update_fields=['status'])
    return redirect(request.META.get('HTTP_REFERER'))


def transfer_to_doing(request, pk):
    task = Task.objects.get(id=pk)
    task.status = 'DO'
    task.save(update_fields=['status'])
    return redirect(request.META.get('HTTP_REFERER'))


def transfer_to_done(request, pk):
    task = Task.objects.get(id=pk)
    task.status = 'DN'
    task.save(update_fields=['status'])
    return redirect(request.META.get('HTTP_REFERER'))


def transfer_to_release(request, pk):
    task = Task.objects.get(id=pk)
    task.status = 'RL'
    task.save(update_fields=['status'])
    return redirect(request.META.get('HTTP_REFERER'))
