from django.utils import timezone

from django.contrib.auth.models import AbstractUser
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.name


class Employee(AbstractUser):
    second_name = models.CharField('Отчество', max_length=255, blank=True, null=True)
    departament = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Отдел', blank=True,  null=True)
    photo = models.ImageField(upload_to='photos_of_employees/%Y/%m/%d/', blank=True, verbose_name='Фотография')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        if self.last_name and self.first_name and self.second_name:
            return f'{self.last_name}\xA0{self.first_name[0]}.\xA0{self.second_name[0]}.'
        return self.username


class Project(models.Model):
    name = models.CharField(max_length=255, verbose_name='Объект')
    about = models.TextField(verbose_name='Описание')
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Комплексный ГИП')

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'

    def __str__(self):
        return self.name


class Task(models.Model):
    todo = 'TD'
    doing = 'DO'
    done = 'DN'
    release = 'RL'

    STATUS = [
        (todo, 'Запланировано'),
        (doing, 'В работе'),
        (done, 'На проверке'),
        (release, 'Завершено')
    ]

    height = 1
    normal = 2
    low = 3
    none = 4

    PRIORITY = [
        (height, 'Высокий приоритет'),
        (normal, 'Средний приоритет'),
        (low, 'Низкий приоритет'),
        (none, 'Приоритет не указан')
    ]

    name = models.CharField(max_length=255, verbose_name='Название')
    about = models.TextField(verbose_name='Описание')
    project = models.ManyToManyField(Project, verbose_name='Объект')
    author_id = models.IntegerField()
    employee = models.ManyToManyField(Employee, verbose_name='Исполнитель')
    status = models.CharField(max_length=2, choices=STATUS, default=todo, verbose_name='Статус')
    priority = models.IntegerField(choices=PRIORITY, default=none, verbose_name='Приоритет')
    start = models.DateField(default=timezone.now)
    end = models.DateField(verbose_name='Окончание')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.name

    def task_todo(self):
        if self.status != 'TD':
            self.status = 'TD'

    def task_doing(self):
        if self.status != 'DO':
            self.status = 'DO'

    def task_done(self):
        if self.status != 'DN':
            self.status = 'DN'

    def task_release(self):
        if self.status != 'RL':
            self.status = 'RL'
