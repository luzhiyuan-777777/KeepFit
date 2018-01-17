from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from baseApp.models import LoginDatas,Point
import datetime
from tools import *
from business import getFirstSightPlan
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    # cookie 验证
    if 'Username' in request.COOKIES:
        username = request.COOKIES.get('Username', '')
        if username:
            return render(request, 'baseApp/index.html')
    return redirect('login_with_args', state='0')

def login(request, **kwargs):
    if 'Username' in request.COOKIES:
        username = request.COOKIES.get('Username', '')
        if username:
            return render(request, 'baseApp/index.html')
    else:
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


def indexForm(request):
    if 'Username' in request.COOKIES:
        sex = request.POST.get('sex', '')
        age = request.POST.get('age', '')
        hurtname = request.POST.get('hurtname', '')
        notright = request.POST.get('notright', '')
        # 分析请求数据 返回前端页面相应值和初视数据
        # TODO 根据部位返回初步诊断建议
        message = {}
        message = {'firstSuggest': 'aaa',
               'sex': sex,
               'age': age,
               'message': message,
               'hurtname': hurtname}
        return render(request, 'baseApp/detail.html', {'Message': message})
    else:
        return render(request, 'baseApp/error.html', {'Message': 'aaa'})

def firstSightForm(request):
    if 'Username' in request.COOKIES:
        sex = request.POST.get('sex', '')
        age = request.POST.get('age', '')
        hurtname = request.POST.get('hurtname', '')
        # 分析请求数据 返回前端页面相应值和推荐治疗穴位
        return render(request, 'baseApp/solution.html', {'finalSuggest':'aaa'})
    else:
        return render(request, 'baseApp/error.html', {'Message': 'aaa'})

@csrf_exempt
def wxUser2Db4Id(request):
    if request.method == 'POST':
        userOpenId = request.POST.get('userOpenId', '')
        userinfo = request.POST.get('res', '')
        if not (userinfo or userOpenId):
            message = {
                'recCode': "failed",
                'openid': ''
            }
            return HttpResponse(json.dumps(message)) # 传输数据丢失
        userInfoJson = string2json(userinfo)
        userid = getWxUserInfo(userOpenId)
        if(userid.count() == 0):
            wxUser2Db(userInfoJson, userOpenId)
        message = {
        'recCode' : "successed",
        'openid' : userOpenId
        }
        return HttpResponse(json.dumps(message))

@csrf_exempt
def wxFirstSight(request):
    if request.method == 'POST':
        userqueryinfo = request.POST.get('queryData', '')
        openid = request.POST.get('openid', '')
        firstsightplan = {}
        if userqueryinfo :
            userqueryinfo = string2json(userqueryinfo)
            userinfo = getWxUserInfo(openid)
            # 根据不舒服的部位信息返回相应的初视治疗信息
            firstsightplan = getFirstSightPlan(userqueryinfo,userinfo)
        # TODO 1 优化微信前端首页页面  2 添加用户搜索表  3 写"初视"页面
        message = {
        'recCode' : "successed",
        'plan' : firstsightplan
        }
        return HttpResponse(json.dumps(message))