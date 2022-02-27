from unicodedata import category
from django.contrib import admin
from .models import TodoList, Category


class TodoAdmin(admin.ModelAdmin):
    fields = ("title", "content", "created", "due_date", "category")


admin.site.register(Category)
admin.site.register(TodoList)
