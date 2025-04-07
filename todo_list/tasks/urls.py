from django.urls import path
from . import views

app_name = "tasks"
urlpatterns = [
    path('create_task/', views.create_task, name="create_task"),
    path('update/<int:task_id/>', views.update_task, name="update_task"),
    path('delete/<int:task_id>/', views.delete_task, name="delete_task"),
    path('success_path/', views.success_path, name="success_path")
]