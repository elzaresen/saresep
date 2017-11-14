# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=1000, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('url', models.CharField(max_length=20, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430')),
                ('date', models.DateTimeField(null=True, verbose_name='\u0414\u0430\u0442\u0430')),
            ],
            options={
                'ordering': ['-date'],
                'db_table': 'videos',
                'verbose_name': '\u0412\u0438\u0434\u0435\u043e',
                'verbose_name_plural': '\u0412\u0438\u0434\u0435\u043e\u043b\u043e\u0440',
            },
        ),
    ]
