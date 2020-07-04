from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.


def index(request):
    # create user
    if request.method == "POST":
        if str(request.user) == "AnonymousUser":
            user = User.objects.create_user(
                username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
            # create additional info in profile
            user.profile.userType = request.POST['userType']
            user.profile.supplyType = request.POST['supplyType']
            user.profile.supplyNumber = request.POST['supplyNumber']
            user.profile.addr = request.POST['address']
            user.profile.tel = request.POST['tel']
            login(request, user)
            return render(request, 'index.html', {"user": request.user, "loggedin": False})
        else:
            user = request.user
            user.profile.userType = request.POST['userType']
            user.profile.supplyType = request.POST['supplyType']
            user.profile.supplyNumber = request.POST['supplyNumber']
            return render(request, 'index.html', {"user": request.user, "loggedin": True})
    if str(request.user) == "AnonymousUser":
        return render(request, 'index.html', {"user": request.user, "loggedin": False})
    else:
        return render(request, 'index.html', {"user": request.user, "loggedin": True})


def home(request):
    if request.method == "POST":
        # do something when user submitted a form
        if str(request.user) != "AnonymousUser":
            body = request.POST["body"]
        else:
            return render(request, "index.html", {"user": request.user, "valid": False})

    return render(request, "index.html", {"user": request.user, "valid": True})


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
    return redirect("/")


def signup_view(request):
    if request.method == "POST":
        user = User.objects.create_user(
            username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
        login(request, user)
        return redirect('/login/')
    return render(request, 'signup.html', {})


def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.supplyType = 'Donor'
    user.save()
