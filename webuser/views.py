from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import *
import bcrypt
from datetime import datetime
# Create your views here.

# 用户登录函数
def login(request):
    if request.method == 'GET':
        uname = request.COOKIES.get('uname', '')
        next_url = request.GET.get('next', '')
        if next_url:
            request.session['next_url'] = next_url
        context = {'title':'用户登录','now_time': datetime.now(), 'error': '0', 'uname': uname}
        return render(request, 'webuser/login.html', context)
    if request.method == 'POST':
        payload = request.POST
        uname = payload.get('name','')
        upwd = payload.get('password','')
        rember = payload.get('remberme',0)
        user = User.objects.filter(uname=uname).values('id','upwd')
        if user and bcrypt.checkpw(upwd.encode(), user[0].get('upwd').encode()):
            request.session['user_id'] = user[0].get('id')
            request.session['user_name'] = uname
            request.session['IS_LOGIN'] = True
            if request.session.get('next_url'):
                return redirect(request.session.get('next_url'))
            red = HttpResponseRedirect('/user/app/')
            if remberme != 0:
                red.set_cookie('uname', uname, max_age=7*24*3600)
            else:
                red.set_cookie('uname', '', max_age=-1)
            return red
        else:
            context = {'title': '用户登录','now_time': datetime.now(), 'error': '1', 'uname': uname, 'upwd': upwd}
            return render(request, 'webuser/login.html', context)

def logout(request):
    request.session.flush()
    return render(request, 'webuser/logout.html')

def reg(request):
    # 加密
    password = bcrypt.hashpw(payload['password'].encode(), bcrypt.gensalt())
    return render(request,'webuser/reg.html')
