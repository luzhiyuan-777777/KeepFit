from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def index(request):
    return render(request, 'baseApp/index.html')

def login(request):
    return render(request, 'baseApp/login.html')

def checkLogin(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    print(username)
    print(password)
    return render(request, 'baseApp/index.html')

def register(request):
    return render(request, 'baseApp/register.html')

def registerIn(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    print(username)
    print(password)
    return render(request, 'baseApp/index.html')