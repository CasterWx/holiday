# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermessage',
            options={'verbose_name': '\u7528\u6237\u7559\u8a00\u4fe1\u606f', 'verbose_name_plural': '\u7528\u6237\u7559\u8a00\u4fe1\u606f'},
        ),
        migrations.RemoveField(
            model_name='usermessage',
            name='id',
        ),
        migrations.AddField(
            model_name='usermessage',
            name='object_id',
            field=models.CharField(default='', max_length=50, serialize=False, primary_key=True),
        ),
        migrations.AlterModelTable(
            name='usermessage',
            table='user_message',
        ),
    ]
