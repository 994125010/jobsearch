# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 22:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='name',
            field=models.CharField(default='EXP', max_length=200),
        ),
    ]
