from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Category, TodoList
import re
def main(request):
    if request.method == "POST":
        if "taskAdd" in request.POST:
            title = request.POST["description"]
            date = str(request.POST['date'])
            category = request.POST["category_select"]
            content = title + " -- " + date + " " + category
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save()
            return redirect("/")
        elif "taskDelete" in request.POST:
            checkedlist = [re.match('checkedbox(?P<id>.*)', s).groupdict()['id'] for s in request.POST.keys() if re.match('checkedbox', s)]
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=todo_id) #getting todo id   
                todo.delete() #deleting todo
            return redirect("/")
        else:
            return HttpResponse("Check Parameters", status=400)
    elif request.method == "GET":

        categories = Category.objects.all()
        todos = TodoList.objects.all()
        return render(request, "works/index.html", {"categories": categories, "todos": todos})



def edit_todo(request, todo_id):
    if request.method == "GET":
        todo = TodoList.objects.get(id=todo_id)
        categories = Category.objects.all()
        todo.due_date = todo.due_date.strftime("%Y-%m-%d")
        return render(request, "works/todo.html", {"todo": todo, "categories": categories})

    elif request.method == "POST":
        title = request.POST["description"]
        date = str(request.POST['date'])
        category = request.POST["category_select"]
        content = title + " -- " + date + " " + category
        todo = TodoList.objects.get(id=todo_id)
        todo.title = request.POST["description"]
        todo.due_date = str(request.POST['date'])
        todo.category = Category.objects.get(name=request.POST["category_select"])
        todo.content = title + " -- " + date + " " + category
        todo.save()
        return redirect("/")

