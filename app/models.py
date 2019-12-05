from django.db import models
from webuser.models import User

# Create your models here.
class Privilege(models.Model):
    user_id = models.ForeignKey(User,on_delete=True)
    p_add = models.BooleanField(u'增加',default=False)
    p_del = models.BooleanField(u'删除',default=False)
    p_chg = models.BooleanField(u'修改',default=False)
    p_sel = models.BooleanField(u'查看',default=False)

class HostInfo(models.Model):
    h_name = models.CharField(u'主机名',max_length=20)
    h_ip = models.CharField(u'IP',max_length=15)
    h_location = models.CharField(u'位置',max_length=10)
    h_virorphy = models.CharField(u'类型',max_length=10)
    h_mem = models.IntegerField(u'内存')
    h_cpu = models.CharField(u'CPU型号',max_length=200)
    h_cpus = models.IntegerField(u'CPU个数')
    h_os = models.CharField(u'操作系统',max_length=100)
    h_status = models.CharField(u'状态',max_length=10,default="运行")

class Monitor(models.Model):
    host_id = models.ForeignKey(HostInfo,on_delete=True)
    m_totalmem = models.IntegerField(u'总内存',default=0)
    m_freemem = models.IntegerField(u'空闲内存',default=0)
    m_useage = models.IntegerField(u'使用率',default=0)
    m_uptime = models.IntegerField(u'运行时间',default=0)

class Service(models.Model):
    STATUS = (
        ('S','STOP'),
        ('R','RUNNING'),
        ('D','DEAD')
    )
    host_id = models.ForeignKey(HostInfo,on_delete=True)
    s_name = models.CharField(u'服务名称',max_length=20)
    s_pid = models.IntegerField(u'PID',)
    s_status = models.CharField(u'运行状态',max_length=1,choices=STATUS)