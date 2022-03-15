from uuid import uuid4
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class TodoList(models.Model):
    id = models.CharField(max_length=300, primary_key=True, default=uuid4)
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, default="generel"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    class Meta:
        ordering = ["-created"]

    def __str__(self) -> str:
        return self.title
