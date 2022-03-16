from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", views.main.as_view()),
    path("todos/<slug:todo_id>", views.edit_todo.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
