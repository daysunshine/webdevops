from django.db import models

# Create your models here.

class User(models.Model):
    uname = models.CharField(u'用户名',unique=True,max_length=20)
    upwd = models.CharField(u'密码',max_length=100)
    uphone = models.CharField(u'电话',max_length=11)

