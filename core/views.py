from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.


def index(request):
    return render(request, "index.html", {})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'login.html', {"isValid": False})
    return render(request, 'login.html', {"isValid": True})


def logout_view(request):
    logout(request)
    return redirect("/login")


def signup_view(request):
    if request.method == "POST":
        user = User.objects.create_user(
            username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
        login(request, user)
        return redirect('/login/')
    return render(request, 'signup.html', {})
