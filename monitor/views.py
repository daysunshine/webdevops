from django.shortcuts import render
from django.http import JsonResponse

from auth.auth import check_login
# Create your views here.
@check_login
def itemhosts(request):
    return JsonResponse({"all_host":""})