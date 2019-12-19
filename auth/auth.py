from django.http import HttpResponseRedirect
from functools import wraps
# from webuser.models import User

def check_login(fn):
    @wraps(fn)
    def wrapper(request,*args,**kwargs):
        login_status = request.session.get('IS_LOGIN', False)
        if login_status:
            return fn(request,*args,*kwargs)
        else:
            # 获取用户当前访问的url，并传递给/user/login/
            next = request.get_full_path()
            red = HttpResponseRedirect('/user/login/?next=' + next)
            return red
    return wrapper

# def check_token(token):
#     if token:
#         serializer = Serializer(secret_key=SECRET_KEY)
#         try:
#             s = serializer.loads(token)
#         except BadSignature as e:
#             # raise exc.HTTPUnauthorized('token is invalid')
#             print(e)
#             # abort(Response('token is invalid', status=401))
#             return False
#         except SignatureExpired as e:
#             # raise exc.HTTPUnauthorized('token is expire')
#             print(e)
#             # abort(Response('token is expire', status=401))
#             return False
#         user = User.objects.filter(id=s['user_id'])[0]
#         return user
