# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class User (models.Model):
    name = models.CharField(max_length=128)
    stuid = models.CharField(max_length=256)
    sex = models.CharField(max_length=32)
    department = models.CharField(max_length=32)
    c_time = models.DateTimeField(auto_now_add=True)
  
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'
class aduser (models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    
    def __str__(self):
        return self.username
    class Meta:
        ordering = ['username']
        verbose_name = '管理员用户'
        verbose_name_plural = '管理员用户'
# Create your models here.
