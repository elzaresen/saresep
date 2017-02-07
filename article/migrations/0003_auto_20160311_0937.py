# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_audio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['slug', '-name'], 'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', 'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.IntegerField(null=True, verbose_name='\u041c\u0435\u0441\u0442\u043e', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='view',
            field=models.IntegerField(default=0, verbose_name='\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u044b'),
        ),
    ]
