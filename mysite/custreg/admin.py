# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from . import models
import sys;
reload(sys);
sys.setdefaultencoding("utf8")
admin.site.register(models.User)
# Register your models here.
