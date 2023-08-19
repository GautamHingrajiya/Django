from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("<h1> Hello </h1>")

def login(request):
    return render(request,"myapp/login.html")