from django.urls import path

from .views import MainView, ProjectView, EmployeeView, TaskDelete, TaskCreate, TaskUpdate, transfer_to_todo, \
    transfer_to_doing, transfer_to_done, transfer_to_release

urlpatterns = [
    path('', MainView.as_view(), name='kanban_page'),
    path('project/<int:pk>', ProjectView.as_view(), name='kanban_project_page'),
    path('employee/<int:pk>', EmployeeView.as_view(), name='kanban_employee_page'),
    # path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/', TaskCreate.as_view(), name='task_create'),
    path('<int:pk>/edit/', TaskUpdate.as_view(), name='task_edit'),
    path('<int:pk>/delete/', TaskDelete.as_view(), name='task_delete'),
    # path('personal/<int:pk>/', PersonalView.as_view(), name='personal'),
    path('todo/<int:pk>', transfer_to_todo, name='transfer_to_todo'),
    path('doing/<int:pk>', transfer_to_doing, name='transfer_to_doing'),
    path('done/<int:pk>', transfer_to_done, name='transfer_to_done'),
    path('release/<int:pk>', transfer_to_release, name='transfer_to_release'),
]
