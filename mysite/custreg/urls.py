# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views
from django.contrib import admin
app_name ='custreg'
urlpatterns =[
	######用户注册页面路由#####
	url(r'^(?P<contest_id>[0-9]+)/$',views.register,name='register'),
	url(r'^reg_user/$',views.reg_user,name='reg_user'),
	url(r'^update_log/$',views.update_log,name='update_log'),
	#####用户管理页面路由#####
	url(r'^ad_login/$',views.ad_login,name='ad_login'),
	url(r'^detail/$',views.detail,name='detail'),
	url(r'^detail/(?P<contest_id>[0-9]+)/$',views.detail,name='detail2'),
	# url(r'^select_user/$',views.select_user,name='select_user'),
	url(r'^del_user/$',views.del_user,name='del_user'),
	url(r'^edit_user/$',views.edit_user,name='edit_user'),
	url(r'^add_user/$',views.add_user,name='add_user'),
	#####比赛管理页面路由#####
	url(r'^contest/$',views.contest,name='contest'),
	url(r'^add_con/$',views.add_con,name='add_con'),
	url(r'^del_con/$',views.del_con,name='del_con'),
	url(r'^edit_con/$',views.edit_con,name='edit_con'),
	url(r'^reg_con/$',views.reg_con,name='reg_con'),
]
