# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20180217_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermessage',
            name='object_id',
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='email',
            field=models.EmailField(default='', max_length=254, serialize=False, verbose_name='\u90ae\u7bb1', primary_key=True),
        ),
    ]
