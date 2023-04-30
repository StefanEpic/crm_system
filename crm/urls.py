from django.urls import path
from django.contrib.auth import views as auth_views

from .views import KanbanView, ProjectView, EmployeeView, DepartmentView, MyView, TaskDelete, transfer_to_todo, \
    transfer_to_doing, transfer_to_done, transfer_to_release, TaskCreate, TaskEdit, ProfileView

urlpatterns = [
    path('', KanbanView.as_view(), name='kanban_page'),
    path('project/<int:pk>', ProjectView.as_view(), name='kanban_project_page'),
    path('employee/<int:pk>', EmployeeView.as_view(), name='kanban_employee_page'),
    path('department/<int:pk>', DepartmentView.as_view(), name='kanban_department_page'),
    path('my/<int:pk>', MyView.as_view(), name='kanban_my_page'),
    path('create/', TaskCreate.as_view(), name='task_create'),
    path('<int:pk>/edit/', TaskEdit.as_view(), name='task_edit'),
    path('<int:pk>/delete/', TaskDelete.as_view(), name='task_delete'),
    path('todo/<int:pk>', transfer_to_todo, name='transfer_to_todo'),
    path('doing/<int:pk>', transfer_to_doing, name='transfer_to_doing'),
    path('done/<int:pk>', transfer_to_done, name='transfer_to_done'),
    path('release/<int:pk>', transfer_to_release, name='transfer_to_release'),

    # path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='profile/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='profile/logout.html'), name='logout'),
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='profile/changepassword.html', success_url='/'), name='change_password'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
]
