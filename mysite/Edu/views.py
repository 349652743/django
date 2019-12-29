# -*- coding:utf-8 -*-
from django.shortcuts import reverse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponse
from django.shortcuts import render,redirect
from django.template import loader
from django.db import connection
from django.http import JsonResponse,Http404
import os
import time
from django.http import FileResponse  
# Create your views here.
def dict_fetchall(cursor):#将游标返回的元组转化为字典，实现方式很独特
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def Teacher(request):
    cursor = connection.cursor()
    cursor.execute('select * from Edu_teacher')
    tea_list = dict_fetchall(cursor)
    #print(tea_list)
    return render(request,'manage/Teacher.html',{'tea_list':tea_list})
def add_tea(request):
    tea=request.POST
    cursor = connection.cursor()
    sql='insert into Edu_teacher(number,name,age,sex,department) values(%d,\"%s\",%d,\"%s\",\"%s\")'%(int(tea['number']),tea['name'],int(tea['age']),tea['sex'],tea['department'])
    #print(sql)
    try:
        cursor.execute(sql)
        response = JsonResponse({'message':'添加成功'})
        return response
    except BaseException as e:
        return JsonResponse({'message':str(e)})
        
def edit_tea(request):
    #print(123)
    tea = request.POST
    cursor = connection.cursor()
    sql = 'update Edu_teacher set name=\"%s\",age=%d,sex=\"%s\",department=\"%s\" where number=%d'%(tea['name'],int(tea['age']),tea['sex'],tea['department'],int(tea['number']))
    #print (sql)
    try:
        cursor.execute(sql)
        response = JsonResponse({'message':'编辑成功'})
        return response
    except BaseException as e:
        print(e)
        return JsonResponse({'message':str(e)})

def dele_tea(request):
    tea = request.POST
    cursor = connection.cursor()
    sql = 'delete from Edu_teacher where number=%d' % (int(tea['number']))
    try:
        cursor.execute(sql)
        response = JsonResponse({'message':'删除成功'})
        return response
    except BaseException as e:
        print(e)
        return JsonResponse({'message':str(e)})
def Classroom(request):
    cursor = connection.cursor()
    cursor.execute('select * from Edu_classroom')
    cla_list = dict_fetchall(cursor)
    return render(request,'manage/Classroom.html',{'cla_list':cla_list})
def add_cla(request):
    cla=request.POST
    cursor = connection.cursor()
    sql='insert into Edu_classroom(number,use_statime,use_endtime,use_course,use_teacher,use_date) values(%d,%d,%d,%d,%d,\"%s\")'%(int(cla['number']),int(cla['use_statime']),int(cla['use_endtime']),int(cla['use_course']),int(cla['use_teacher']),cla['use_date'])
    print(sql)
    try:
        cursor.execute(sql)
        response = JsonResponse({'message':'添加成功'})
        return response
    except BaseException as e:
        return JsonResponse({'message':str(e)})
        
def edit_cla(request):
    #print(123)
    cla = request.POST
    cursor = connection.cursor()
    sql = 'update Edu_classroom set use_statime=%d,use_endtime=%d,use_course=%d,use_teacher=%d,use_date=\"%s\" where number=%d'%(int(cla['use_statime']),int(cla['use_endtime']),int(cla['use_course']),int(cla['use_teacher']),cla['use_date'],int(cla['number']))
    #print (sql)
    try:
        cursor.execute(sql)
        response = JsonResponse({'message':'编辑成功'})
        return response
    except BaseException as e:
        print(e)
        return JsonResponse({'message':str(e)})

def dele_cla(request):
    cla = request.POST
    cursor = connection.cursor()
    sql = 'delete from Edu_classroom where number=%d' % (int(cla['number']))
    try:
        cursor.execute(sql)
        response = JsonResponse({'message':'删除成功'})
        return response
    except BaseException as e:
        print(e)
        return JsonResponse({'message':str(e)})
    
def Course(request):
    cursor = connection.cursor()
    cursor.execute('select * from Edu_course')
    cou_list = dict_fetchall(cursor)
    return render(request,'manage/Course.html',{'cou_list':cou_list})
def add_cou(request):
    cou=request.POST
    cursor = connection.cursor()
    sql='insert into Edu_course(number,tea_number,tea_name,sta_time,end_time,date) values(%d,%d,\"%s\",%d,%d,\"%s\")'%(int(cou['number']),int(cou['tea_number']),cou['tea_name'],int(cou['sta_time']),int(cou['end_time']),cou['date'])
    print(sql)
    try:
        cursor.execute(sql)
        response = JsonResponse({'message':'添加成功'})
        return response
    except BaseException as e:
        return JsonResponse({'message':str(e)})
        
def edit_cou(request):
    #print(123)
    cou = request.POST
    cursor = connection.cursor()
    sql = 'update Edu_course set tea_number=%d,tea_name=\"%s\",sta_time=%d,end_time=%d,date=\"%s\" where number=%d'%(int(cou['tea_number']),cou['tea_name'],int(cou['sta_time']),int(cou['end_time']),cou['date'],int(cou['number']))
    #print (sql)
    try:
        cursor.execute(sql)
        response = JsonResponse({'message':'编辑成功'})
        return response
    except BaseException as e:
        print(e)
        return JsonResponse({'message':str(e)})

def dele_cou(request):
    cou = request.POST
    cursor = connection.cursor()
    sql = 'delete from Edu_course where number=%d' % (int(cou['number']))
    try:
        cursor.execute(sql)
        response = JsonResponse({'message':'删除成功'})
        return response
    except BaseException as e:
        print(e)
        return JsonResponse({'message':str(e)})
def select(request):
    if request.is_ajax():
        tmp=request.POST
        print(tmp['number'])
        print(tmp['option'])
        if tmp['option']=='option1':
            cursor = connection.cursor()
            cursor.execute('select * from Edu_teacher where number=%d'%int(tmp['number']))
            tea_list = dict_fetchall(cursor)
            #print(tea_list)
            return JsonResponse({'tea_list':tea_list})
        elif tmp['option']=='option2':
            cursor = connection.cursor()
            cursor.execute('select * from Edu_classroom where number=%d'%int(tmp['number']))
            cla_list = dict_fetchall(cursor)
            #print(tea_list)
            return JsonResponse({'cla_list':cla_list})
        else:
            cursor = connection.cursor()
            cursor.execute('select * from Edu_course where number=%d'%int(tmp['number']))
            cou_list = dict_fetchall(cursor)
            #print(tea_list)
            return JsonResponse({'cou_list':cou_list})
    return render(request,'function/select.html')
def backup(request):
    if  request.is_ajax:
        option=request.POST.get('option')
        if(option=='1'):
            str1='/home/backup/'
            str2='mysite_'+time.strftime("%Y_%m_%d__%H_%M_%S", time.localtime())+'.sql'
            try:
                os.system('mysqldump -uroot -p123456 mysite > '+str1+str2)
                
                print(str2)
                with open('/home/backup/backup.txt', 'r+') as f:
                    content = f.read()      
                    f.seek(0, 0)
                    f.write(str2+'\n'+content)
                response = JsonResponse({'message':"备份成功"})
                return response
            except:
                response = JsonResponse({'message':'备份失败'})
                return response
        elif(option=='2'):
            str=''
            try:
                with open('/home/backup/backup.txt', 'r') as f:
                    lines = f.readlines()
                    str = lines[0]
                print(str)
                recoverycmd = "mysql -u" +'root' + " -p"+'123456'+" " +'mysite'+" < "+'/home/backup/'+str
                os.system(recoverycmd)
                response = JsonResponse({'message':"恢复成功"})
                return response
            except:
                response = JsonResponse({'message':'恢复失败'})
                return response
    return render(request,'function/backup.html')