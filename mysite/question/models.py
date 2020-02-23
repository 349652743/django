# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class question (models.Model):
    title = models.CharField(max_length=256)
    option1 = models.CharField(max_length=256)
    option2 = models.CharField(max_length=256)
    option3 = models.CharField(max_length=256)
    option4 = models.CharField(max_length=256)
    question_type = models.IntegerField()
    answer = models.CharField(max_length=256)
    username = models.CharField(max_length=128)
    def __str__(self):
        return self.title