from django.urls import path
from . import views

urlpatterns = [
    path("", views.main),
    path("todos/<slug:todo_id>", views.edit_todo)
]