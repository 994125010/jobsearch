# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 00:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_experience_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(verbose_name='end date'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_date',
            field=models.DateField(verbose_name='start date'),
        ),
    ]
