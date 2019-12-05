from django.http import HttpResponseRedirect
from functools import wraps

def check_login(fn):
    @wraps(fn)
    def wrapper(request,*args,**kwargs):
        if request.session.get('IS_LOGIN', False):
            return fn(request,*args,*kwargs)
        else:
            # 获取用户当前访问的url，并传递给/user/login/
            next = request.get_full_path()
            red = HttpResponseRedirect('/user/login/?next=' + next)
            return red
    return wrapper