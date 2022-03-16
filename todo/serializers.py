from rest_framework import serializers
from . import models


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Category
        fields = "__all__"

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TodoList
        fields = "__all__"
        level = 1


