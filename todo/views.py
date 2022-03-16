import re

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from .models import Category, TodoList
from django.utils.decorators import method_decorator
from .serializers import TodoSerializer, CategoriesSerializer
import ujson


@method_decorator(login_required(login_url="/users/signIn/"), name="dispatch")
class main(APIView):
    queryset = TodoList.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        if "taskAdd" in request.POST:
            serializer = TodoSerializer(data=ujson.loads(request.data))
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif "taskDelete" in request.POST:
            checkedlist = [
                re.match("checkedbox(?P<id>.*)", s).groupdict()["id"]
                for s in request.POST.keys()
                if re.match("checkedbox", s)
            ]
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=todo_id)  # getting todo id
                todo.delete()  # deleting todo
            return redirect("/")
        else:
            return HttpResponse("Check Parameters", status=400)

    def get(self, request, format=None):

        todos = TodoList.objects.filter(user=request.user)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@method_decorator(login_required(login_url="/users/signIn/"), name="dispatch")
class edit_todo(APIView):
    def get(self, request, todo_id, format=None):
        todo = TodoList.objects.get(id=todo_id, user=request.user)
        todo.due_date = todo.due_date.strftime("%Y-%m-%d")
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, todo_id, format=None):
        todo = TodoList.objects.get(id=todo_id, user=request.user)
        serializer = TodoSerializer(todo, data=ujson.loads(request.data))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
