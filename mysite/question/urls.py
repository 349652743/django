# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views
app_name ='question'
urlpatterns = [
    url(r'^reg/$',views.reg,name='reg'),
    url(r'^log/$',views.log,name='log'),
    url(r'^detail/$',views.detail,name='detail'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^add_wrong/$',views.add_wrong,name='add_wrong'),
    url(r'^erase_wrong/$',views.erase_wrong,name='erase_wrong'),
    url(r'^detail/(?P<question_id>[0-9]+)/$',views.detail,name='detail2'),
]
