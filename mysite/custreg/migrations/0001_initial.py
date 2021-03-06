# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-18 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('stuid', models.CharField(max_length=256)),
                ('sex', models.CharField(choices=[('male', '\u7537'), ('female', '\u5973')], default='\u7537', max_length=32)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['c_time'],
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
        ),
    ]
