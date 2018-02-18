# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_auto_20180217_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermessage',
            name='email',
            field=models.CharField(default='', max_length=100, serialize=False, verbose_name='\u90ae\u7bb1', primary_key=True),
        ),
        migrations.AlterModelTable(
            name='usermessage',
            table=None,
        ),
    ]
