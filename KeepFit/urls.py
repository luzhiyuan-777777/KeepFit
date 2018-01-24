"""KeepFit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from baseApp import views as baseView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', baseView.index,name="index"),
    url(r'^login/$', baseView.login,name="login"),
    url(r'^login/(?P<state>\w{1})/$',baseView.login, name='login_with_args'),
    url(r'^checkLogin/', baseView.checkLogin,name="checkLogin"),
    url(r'^register/$', baseView.register,name="register"),
    url(r'^registerIn/', baseView.registerIn,name="registerIn"),
    url(r'^register/(?P<state>\w{1})/$',baseView.register, name='register_with_args'),
    url(r'^indexForm/', baseView.indexForm,name="indexForm"),
    url(r'^firstSightForm/', baseView.firstSightForm,name="firstSightForm"),
    url(r'^wx/user2Db4Id/', baseView.wxUser2Db4Id,name="wxUser2Db4Id"),
    url(r'^wx/firstSight/', baseView.wxFirstSight,name="wxFirstSight"),
    url(r'^wx/firstPlan/', baseView.wxFirstPlan,name="wxFirstPlan"),
]
