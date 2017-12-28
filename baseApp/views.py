from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from baseApp.models import LoginDatas
import datetime
from tools import *
# Create your views here.
def index(request):
    # cookie 验证
    return render(request, 'baseApp/index.html')

def login(request, **kwargs):
    state = ''
    if kwargs:
        state = str(kwargs['state'])
    else:
        print('no kwargs in login')
    return render(request, 'baseApp/login.html', {'state': state})

def checkLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        isuser = getUserPassword(username,password)
        if ("1" == isuser):
            # 写cookie
            response = redirect('index')
            response.set_cookie(
                'Username', username, expires=datetime.datetime.now() +datetime.timedelta(days=3))
            return response
        else:
            # 提示账号密码错误
            return redirect('login_with_args', state='1')

def register(request):
    return render(request, 'baseApp/register.html')

def registerIn(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    userdata = LoginDatas(Username=username, Password=password)
    userdata.save()
    # 写cookie
    return render(request, 'baseApp/index.html')