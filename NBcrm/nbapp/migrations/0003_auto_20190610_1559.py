# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-06-10 07:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nbapp', '0002_auto_20190610_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='consultant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='销售'),
        ),
    ]
