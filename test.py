# from django.http import HttpResponseRedirect
#
# from django.contrib import  auth
# from django.contrib.auth.decorators import login_required
# from app.models import HostInfo
# #
# import bcrypt
#
# a = '$2b$12$EjkudLxAsQtFJLGWwI6vFOSl117cfFoj8/vBxeg/cVqmqPXXwYLzC'
#
# b = bcrypt.checkpw('12345678'.encode(), a.encode())
# print(b)

# cc = bcrypt.hashpw('12345678'.encode(), bcrypt.gensalt())
# print(cc)


# lists = HostInfo.objects.filter(id=1)
#
# print(lists)


a = {'1':'asda','sa':123}

a.pop('1')

print(len(a))

