# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-04 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0034_auto_20180401_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentproperty',
            name='value',
            field=models.TextField(),
        ),
    ]