from django.urls import path
from . import views

urlpatterns = [
    path("", views.main.as_view()),
    path("todos/<slug:todo_id>", views.edit_todo.as_view())
]