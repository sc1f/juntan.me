# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 00:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20170801_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermeta',
            name='resume',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]