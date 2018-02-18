# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u7528\u6237\u540d')),
                ('email', models.EmailField(max_length=254, verbose_name='\u90ae\u7bb1')),
                ('adress', models.CharField(max_length=200, verbose_name='\u8054\u7cfb\u5730\u5740')),
                ('message', models.CharField(max_length=500, verbose_name='\u7559\u8a00\u4fe1\u606f')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u7559\u8a00\u4fe1\u606f',
            },
        ),
    ]
