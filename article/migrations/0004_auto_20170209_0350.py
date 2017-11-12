# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20160311_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='cart',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[('1', '\u0411\u0438\u0440\u0438\u043d\u0447\u0438'), ('2', '\u042d\u043a\u0438\u043d\u0447\u0438'), ('3', '\u04ae\u0447\u04af\u043d\u0447\u04af'), ('4', '\u0422\u04e9\u0440\u0442\u04af\u043d\u0447\u04af'), ('5', '\u0411\u0435\u0448\u0438\u043d\u0447\u0438')]),
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(null=True, verbose_name='\u0414\u0430\u0442\u0430'),
        ),
    ]
