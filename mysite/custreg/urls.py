# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views
from django.contrib import admin
app_name ='custreg'
urlpatterns =[
	######用户注册页面路由#####
	url(r'^register/$',views.register,name='register'),
	url(r'^reg_user/$',views.reg_user,name='reg_user'),
	url(r'^update_log/$',views.update_log,name='update_log'),
	#####后台管理页面路由#####
	url(r'^ad_login/$',views.ad_login,name='ad_login'),
	url(r'^detail/$',views.detail,name='detail'),
	url(r'^del_user/$',views.del_user,name='del_user'),
	url(r'^edit_user/$',views.edit_user,name='edit_user'),
	url(r'^add_user/$',views.add_user,name='add_user'),
]
