from unicodedata import category
from rest_framework import serializers
from . import models


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Category
        fields = "__all__"

class TodoSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field="username")
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = models.TodoList
        fields = "__all__"


