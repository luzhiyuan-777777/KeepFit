from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from baseApp.models import LoginDatas
import datetime
from tools import *
# Create your views here.
def index(request):
    # cookie 验证
    if 'Username' in request.COOKIES:
        username = request.COOKIES.get('Username', '')
        if username:
            return render(request, 'baseApp/index.html')
    return redirect('login_with_args', state='0')

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
            return writeCookie(request,username)
        else:
            # 提示账号密码错误
            return redirect('login_with_args', state='1')

def register(request,**kwargs):
    state = ''
    if kwargs:
        state = str(kwargs['state'])
    else:
        print('no kwargs in register')
    return render(request, 'baseApp/register.html',{'state': state})

def registerIn(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    # 判断是否有该用户 有则返回数据
    userindb = isUserInDb(username)
    if ("1" == userindb):
        return redirect('register_with_args', state='1')
    else:
        # 没有则添加到库
        userdata = LoginDatas(Username=username, Password=password)
        userdata.save()
        # 写cookie
        return writeCookie(request, username)

def writeCookie(request,username):
    # 写cookie 跳转到首页
    response = redirect('index')
    response.set_cookie(
        'Username', username, expires=datetime.datetime.now() + datetime.timedelta(days=3))
    return response