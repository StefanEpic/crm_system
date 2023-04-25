from django.urls import path

from .views import MainView, ProjectView, EmployeeView, TaskUpdate, TaskDelete

urlpatterns = [
    path('', MainView.as_view(), name='kanban_page'),
    path('project/<int:pk>', ProjectView.as_view(), name='kanban_project_page'),
    path('employee/<int:pk>', EmployeeView.as_view(), name='kanban_employee_page'),
    # path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    # path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/edit/', TaskUpdate.as_view(), name='task_edit'),
    path('<int:pk>/delete/', TaskDelete.as_view(), name='task_delete'),
    # path('personal/<int:pk>/', PersonalView.as_view(), name='personal'),
    # path('upgrade/', upgrade_me, name='upgrade'),
]
