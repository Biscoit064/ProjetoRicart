from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.tasklist, name='tasklist'),
    path('task/<int:id>', views.taskview, name='task-view'),
]
