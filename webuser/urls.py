from django.urls import path,include
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.login),
    url('^login/$',views.login,name='login'),
    url('^logout/$',views.logout,name='logout'),
]