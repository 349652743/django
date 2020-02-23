# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,HttpResponse,redirect,reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.core import serializers
from . import models
import json
import datetime
from django.contrib.auth.models import auth,User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
def log(request):
    if request.is_ajax():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return JsonResponse({'message':'登陆成功'})
        else:
            # Return an 'invalid login' error message.
            return JsonResponse({'message':'登陆失败'})
    else:
        return render(request,'log.html')
def reg(request):
    if request.is_ajax():
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username = username , password = password)
            return JsonResponse({'message':'注册成功'})
        except BaseException as e:
            return JsonResponse({'message':str(e)})
    else:
        return render(request,'reg.html')
def detail(request,question_id=-1):
    # print(request.user)
    if  not  request.user.is_authenticated():
        return  redirect('/question/log')
    else:
        if question_id == -1:
            question_list = models.question.objects.filter(username='root').filter(question_type='1').order_by('?')[:50]
            mul_question_list = models.question.objects.filter(username='root').filter(question_type='2').order_by('?')[:30]
            tf_question_list = models.question.objects.filter(username='root').filter(question_type='3').order_by('?')[:20]
            return render(request,'detail.html',{'question_list':question_list,'mul_question_list':mul_question_list,'tf_question_list':tf_question_list})
        elif question_id == '0':
            question_list = models.question.objects.filter(username=request.user).filter(question_type='1').order_by('?')[:50]
            mul_question_list = models.question.objects.filter(username=request.user).filter(question_type='2').order_by('?')[:30]
            tf_question_list = models.question.objects.filter(username=request.user).filter(question_type='3').order_by('?')[:20]
            print(type(question_list))
            return render(request,'detail.html',{'question_list':question_list,'mul_question_list':mul_question_list,'tf_question_list':tf_question_list})
        elif question_id == '1':
            question_list = models.question.objects.filter(username=request.user).filter(question_type='1')
            mul_question_list = models.question.objects.filter(username=request.user).filter(question_type='2')
            tf_question_list = models.question.objects.filter(username=request.user).filter(question_type='3')
            return render(request,'detail.html',{'question_list':question_list,'mul_question_list':mul_question_list,'tf_question_list':tf_question_list})
def add_wrong(request):
    data=request.POST.getlist('title');
    for i in data:
        question_list =models.question.objects.filter(username=request.user).filter(title=i)
        if not question_list:
            tmp=models.question.objects.filter(title=i).first()
            models.question.objects.create(
				title = tmp.title,
                option1 = tmp.option1,
                option2 = tmp.option2,
                option3 = tmp.option3,
                option4 = tmp.option4,
                question_type = tmp.question_type,
                answer = tmp.answer,
                username = request.user,
			)
            return JsonResponse({'message':'添加成功'})
    return JsonResponse({'message':'添加失败'})
def erase_wrong(request):
    data=request.POST.getlist('title');
    for i in data:
        question_list =models.question.objects.filter(username=request.user).filter(title=i).delete()
        return JsonResponse({'message':'删除成功'})
def logout(request):
    auth.logout(request)
    return redirect('/question/log')