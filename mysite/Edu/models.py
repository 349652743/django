# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class Teacher(models.Model):
    number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 200)
    age = models.IntegerField(default = 0)
    sex = models.CharField(max_length = 200)
    department = models.CharField(max_length = 200)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['number']
class Course(models.Model):
    number = models.IntegerField(primary_key=True)
    tea_number = models.IntegerField(default = 0)
    tea_name = models.CharField(max_length = 200)
    sta_time = models.IntegerField(default = 0)
    end_time = models.IntegerField(default = 0)
    date = models.CharField(max_length = 200)
    class Meta:
        ordering = ['date']
class Classroom(models.Model):
    number = models.IntegerField(primary_key=True)
    use_statime = models.IntegerField(default = 0)
    use_endtime = models.IntegerField(default = 0)
    use_course = models.IntegerField(default = 0)
    use_teacher = models.IntegerField(default = 0)
    use_date = models.CharField(max_length = 200)