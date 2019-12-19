from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.db import transaction
from django.http import JsonResponse
from .models import *
from auth.auth import check_login

@check_login
def index(request):
    context = {'uname':request.session.get('uname')}
    return render(request,'webuser/index.html',context)

@check_login
def hostlist(request):
    context = {'uname': request.session.get('uname')}
    return render(request,'webuser/hostlist.html',context)
    # return 'webuser/hostlist.html'

@check_login
def handle_hostlist(request):
    if request.method == 'GET':
        # limit = int(request.GET.get('limit',14))
        # offset = int(request.GET.get('offset',0))
        # print(limit,offset)
        pageSize = int(request.GET.get('pageSize',10)) # 每页10条
        pageNumber = int(request.GET.get('pageNumber',1)) # 默认第一页
        all_records = HostInfo.objects.all().values()
        # 创建分页对象
        pagenator = Paginator(all_records,pageSize)
        try:
            pages = pagenator.page(pageNumber)
        except Exception as e:
            pages = pagenator.page(1) if pageNumber < 2 else pagenator.page(pageNumber - 1)
        # print(pagenator.page(pageNumber))
        # part_list = list(lists)[offset:limit]
        # print(part_list)
        count = all_records.count()
        ret = {'total':count,'rows':[record for record in pages]}
        return JsonResponse(ret)

@check_login
def updatehost(request):
    if request.method == "POST":
        payload = request.POST
        id = payload.get('pk_id',None)
        h_name = payload.get('u_hostname',None)
        h_ip = payload.get('u_address',None)
        h_location = payload.get('u_location',None)
        h_virorphy = payload.get('u_host_type',None)
        h_mem = payload.get('u_memory',None)
        h_cpu = payload.get('u_cpu_v',None)
        h_cpus = payload.get('u_cpu_num',None)
        h_os = payload.get('u_os',None)
        h_status = payload.get('u_status',None)
        # print(id,h_name,h_ip,h_location,h_virorphy,h_mem,h_cpu,h_cpus,h_os,h_status)
        if all([id,h_name,h_ip,h_location,h_virorphy,h_mem,h_cpu,h_cpus,h_os,h_status]):
            try:
                host = HostInfo.objects.filter(id=id)[0]
                host.h_name = h_name
                host.h_ip = h_ip
                host.h_location = h_location
                host.h_virorphy = h_virorphy
                host.h_mem = h_mem
                host.h_cpu = h_cpu
                host.h_cpus = h_cpus
                host.h_os = h_os
                host.h_status = h_status
            except Exception as e:
                # print(e)
                return JsonResponse({'error':1,'message':'Not Found Host Id!!!'})
            try:
                with transaction.atomic():
                    host.save()
            except Exception as e:
                print(e)
                return JsonResponse({'error': 1, 'message': 'system error!!!'})
            return JsonResponse({'error': 0, 'message': 'Update Success'})

@check_login
def delhost(request):
    if request.method == 'POST':
        payload = request.POST
        ids = eval(payload.get('ids',None)) # tuple
        if ids:
            for id in ids:
                try:
                    with transaction.atomic():
                        host = HostInfo.objects.filter(id=id).delete()
                except Exception as e:
                    print('eeee',e)
                    return JsonResponse({'error': 1, 'message': 'Error!!!'})
            return JsonResponse({'error': 0, 'message': 'Delete Success!!!'})
        return JsonResponse({'error': 1, 'message': 'None id !!!'})
    return JsonResponse({'error': 1, 'message': 'Only Support POST Method!!!'})

@check_login
def addhost(request):
    if request.method == "POST":
        payload = request.POST
        h_name = payload.get('c_hostname', None)
        h_ip = payload.get('c_address', None)
        h_location = payload.get('c_location', None)
        h_virorphy = payload.get('c_host_type', None)
        h_mem = payload.get('c_memory', None)
        h_cpu = payload.get('c_cpu_v', None)
        h_cpus = payload.get('c_cpu_num', None)
        h_os = payload.get('c_os', None)
        h_status = payload.get('c_status', None)
        # print(id,h_name,h_ip,h_location,h_virorphy,h_mem,h_cpu,h_cpus,h_os,h_status)
        if all([h_name, h_ip, h_location, h_virorphy, h_mem, h_cpu, h_cpus, h_os, h_status]):
            try:
                host = HostInfo()
                host.h_name = h_name
                host.h_ip = h_ip
                host.h_location = h_location
                host.h_virorphy = h_virorphy
                host.h_mem = h_mem
                host.h_cpu = h_cpu
                host.h_cpus = h_cpus
                host.h_os = h_os
                host.h_status = h_status
            except Exception as e:
                # print(e)
                return JsonResponse({'error': 1, 'message': 'Add Error !!!'})
            try:
                with transaction.atomic():
                    host.save()
            except Exception as e:
                print(e)
                return JsonResponse({'error': 1, 'message': 'system error!!!'})
            return JsonResponse({'error': 0, 'message': 'Add Success'})
        else:
            return JsonResponse({'error': 1, 'message': 'The information is not complete !!!'})





