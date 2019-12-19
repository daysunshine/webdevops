from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import *
import bcrypt
from datetime import datetime
# Create your views here.
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# from webdevops.settings import SECRET_KEY

# 获取token
# def gen_token(user_id):
#     serializer = Serializer(secret_key=SECRET_KEY, expires_in=3600)
#     token = serializer.dumps({"user_id": user_id}).decode()
#     return token

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
        remberme = payload.get('remberme',0)
        user = User.objects.filter(uname=uname).values('id','upwd')
        # if user and bcrypt.checkpw(upwd.encode(), user[0].get('upwd').encode()):
        if uname == "admin" and upwd == "admin":
            # request.session['user_id'] = user[0].get('id')
            request.session['uname'] = uname
            request.session['IS_LOGIN'] = True
            request.session.set_expiry(3600)
            if request.session.get('next_url'):
                return redirect(request.session.get('next_url'))
            red = HttpResponseRedirect('/app/')
            # red.set_cookie('sessionid', gen_token(user[0].get('id')), max_age=3600)
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
    request.session.delete()
    return render(request, 'webuser/logout.html')

def reg(request):
    # 加密
    password = bcrypt.hashpw(payload['password'].encode(), bcrypt.gensalt())
    return render(request,'webuser/reg.html')
