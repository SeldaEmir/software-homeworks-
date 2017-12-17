from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from untitled2.models import entrylist

# Create your views here.

def signup(request):

    if request.method == "POST":
        User.objects.create_user(username=request.POST.get("username"),
                            password=request.POST.get("password"))
        return HttpResponse("Success!")
    return render(request, "register.html")

def login(request):
    if request.method == "POST":
        return render(request,"forListAll.txt", {"list":entrylist})
    return render(request, "login.html")

