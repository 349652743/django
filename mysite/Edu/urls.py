# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views
app_name ='Edu'
urlpatterns = [
    url(r'^Course/$',views.Course,name='Course'),
    url(r'^add_cou/$',views.add_cou,name='add_cou'),
    url(r'^edit_cou/$',views.edit_cou,name='edit_cou'),
    url(r'^dele_cou/$',views.dele_cou,name='dele_cou'),
    url(r'^Classroom/$',views.Classroom,name='Classroom'),
    url(r'^add_cla/$',views.add_cla,name='add_cla'),
    url(r'^edit_cla/$',views.edit_cla,name='edit_cla'),
    url(r'^dele_cla/$',views.dele_cla,name='dele_cla'),
    url(r'^Teacher/$',views.Teacher,name='Teacher'),
    url(r'^add_tea/$',views.add_tea,name='add_tea'),
    url(r'^edit_tea/$',views.edit_tea,name='edit_tea'),
    url(r'^dele_tea/$',views.dele_tea,name='dele_tea'),

    url(r'^select/$',views.select,name='select'),

    url(r'^backup/$',views.backup,name='backup'),
]
