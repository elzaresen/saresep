# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=1000, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('body', redactor.fields.RedactorField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
                ('view', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
                ('rate', models.IntegerField(default=0)),
                ('date', models.DateTimeField(null=True, verbose_name='\u0414\u0430\u0442\u0430', blank=True)),
                ('keys', models.CharField(max_length=1000, null=True, verbose_name='\u041a\u043b\u044e\u0447\u0438', blank=True)),
                ('published', models.BooleanField(default=False, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d')),
                ('category', models.ForeignKey(verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', to='article.Category')),
            ],
            options={
                'ordering': ['-date'],
                'db_table': 'news',
                'verbose_name': '\u041d\u043e\u0432\u043e\u0441\u0442\u044c',
                'verbose_name_plural': '\u041d\u043e\u0432\u043e\u0441\u0442\u0438',
            },
        ),
        migrations.CreateModel(
            name='NewsComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=100, verbose_name='\u0412\u0430\u0448\u0435 \u0438\u043c\u044f')),
                ('text', models.TextField(verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('relation', models.ForeignKey(to='news.News')),
            ],
            options={
                'db_table': 'news_comment',
                'verbose_name': '\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439',
                'verbose_name_plural': '\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438',
            },
        ),
    ]
