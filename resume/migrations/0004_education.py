# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20160228_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=200)),
                ('major', models.CharField(max_length=500)),
                ('gpa', models.CharField(max_length=3)),
            ],
        ),
    ]
