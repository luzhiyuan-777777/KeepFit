from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from baseApp.models import LoginDatas
from tools import *
# Create your views here.
def index(request):
    # cookie 验证
    return render(request, 'baseApp/index.html')

def login(request):
    return render(request, 'baseApp/login.html')

def checkLogin(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    isuser = getUserPassword(username,password)
    if ("1"==isuser):
        # 写cookie
        return render(request, 'baseApp/index.html')
    else:
        # 提示账号密码错误
        return render(request, 'baseApp/login.html')

def register(request):
    return render(request, 'baseApp/register.html')

def registerIn(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    userdata = LoginDatas(Username=username, Password=password)
    userdata.save()
    # 写cookie
    return render(request, 'baseApp/index.html')