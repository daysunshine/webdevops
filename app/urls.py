from django.urls import path,include
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.index,name='index'),
    # url('^index/$',views.index,name='index'),
    url('^hostlist/$',views.hostlist,name='hostlist'),
    url('^handle_hostlist/$',views.handle_hostlist,name='handle_hostlist'),
    url('^updatehost/$',views.updatehost,name='updatehost'),
    url('^delhost/$',views.delhost,name='delhost'),
    url('^addhost/$',views.addhost,name='addhost'),
]

