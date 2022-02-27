from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def sign_up(request):
    # handle new user creation
    if request.method == "POST":
        if (
            "username" in request.POST
            and "pass" in request.POST
            and "email" in request.POST
        ):
            username = request.POST["username"]
            password = request.POST["pass"]
            email = request.POST["email"]
            first_name = request.POST["name"]
            # last_name = request.POST["last_name"]
            u = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                # last_name=last_name,
            )
            return redirect("/users/signIn")
        else:
            return HttpResponse("check params", status=400)
    # give sign up form to client
    elif request.method == "GET":
        return render(request, "users/signUp.html")


def sign_in(request):
    # sign-in form
    if request.method == "GET":
        return render(request, "users/signIn.html")
    # login user
    elif request.method == "POST":
        if "username" in request.POST and "pass" in request.POST:
            user = authenticate(
                request,
                username=request.POST["username"],
                password=request.POST["pass"],
            )
            if user is not None:
                login(request, user)
                return redirect("/users/dashboard/")
            else:
                return HttpResponse(
                    "check credentials", status=404
                )
        else:
            return HttpResponse("check params", status=400)

@login_required
def dashboard(request):
    return render(request, "users/dashboard.html", {"email": request.user.email, "username": request.user.username})