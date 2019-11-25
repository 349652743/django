# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect,reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from . import models

# url(r'^ad_login/$',views.ad_login,name='ad_login'),
# 	url(r'^detail/$',views.detail,name='detail'),
# 	url(r'^register/$',views.register,name='register'),
# 	url(r'^admin',admin.site.urls),
#路由列表
#####后台管理页面#####
def login_auth(func):#登录验证装饰器
	def wrapper(request,*args,**kwargs):
		is_login=request.session.get('is_login',None)
		if is_login:
			return func(request,*args,**kwargs)
		else:
			return redirect(reverse('custreg:ad_login'))
	return wrapper

def ad_login(request):#管理员登录
	if request.is_ajax():
		aduser=request.POST
		#print(aduser)
		try:
			user=models.aduser.objects.get(username=aduser['username'])
			if(user.password==aduser['password']):
				request.session['is_login'] = True
				request.session.set_expiry(0)
				response=JsonResponse({'message':'登陆成功'})	#ajax 无法重定向，所以通过前端跳转
				return response
			else:
				response = JsonResponse({'message':'密码错误'})
				return response
		except:
			response = JsonResponse({'message':'用户未注册'})
			return response
	return render(request,'cust_admin/ad_login.html')
@login_auth
def detail(request):#后台页面
	stu_list = models.User.objects.all()
	return render(request,'cust_admin/detail.html',{'stu_list':stu_list})
@login_auth
def del_user(request):#用户删除
	userid=request.POST.get('userid')
	try:
		models.User.objects.filter(id=userid).delete()
		response=JsonResponse({'status':True})
		return response
	except:
		response=JsonResponse({'status':False})
		return response
@login_auth
def edit_user(request):#用户编辑
	user=request.POST
	try:
		#print(user)
		models.User.objects.filter(id=user['nid']).update(
			name=user['user'],
			stuid=user['stuid'],
			sex=user['sex'],
			department=user['department']
		)
		response=JsonResponse({'status':True})
		return response
	except Exception as e:
		#print(e);
		response=JsonResponse({'status':False})
		return response
@login_auth
def add_user(request): #添加用户
	stuD=request.POST
	#print(123);
	try:
		models.User.objects.get(stuid=stuD['stuid'])
		response=JsonResponse({'message':'用户已注册,请勿重复添加'})
		return response
	except:
		try:
			#print(stuD)
			models.User.objects.create(
				name = stuD['name'],
				department = stuD['department'],
				sex = stuD['sex'],
				stuid = stuD['stuid']
			)
			response=JsonResponse({'message':"添加成功"})
			return response
		except:
			response=JsonResponse({'message':'添加失败'})
			return response
#####用户注册页面#####
def register(request):
	return render(request,'cust_user/register.html')

def reg_user(request):
	stuD=request.POST
	try:
		# print(stuD)
		models.User.objects.get(stuid=stuD['stuid'])
		response=JsonResponse({'message':'学号已注册,请勿重复注册'})
		return response
	except:
		try:
			models.User.objects.create(
				name = stuD['name'],
				department = stuD['department'],
				sex = stuD['sex'],
				stuid = stuD['stuid']
			)
			response=JsonResponse({'message':"注册成功"})
			return response
		except:
			response=JsonResponse({'message':"注册失败"})
			return response
def update_log(request):
    return render(request,'cust_user/update_log.html')



