# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields
import article.models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=1000, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('body', redactor.fields.RedactorField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
                ('cart', models.CharField(blank=True, max_length=1, null=True, choices=[('1', '\u0411\u0438\u0440\u0438\u043d\u0447\u0438'), ('2', '\u042d\u043a\u0438\u043d\u0447\u0438'), ('3', '\u04ae\u0447\u04af\u043d\u0447\u04af'), ('4', '\u0422\u04e9\u0440\u0442\u04af\u043d\u0447\u04af')])),
                ('rate', models.IntegerField(default=0)),
                ('view', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
                ('date', models.DateTimeField(null=True, verbose_name='\u0414\u0430\u0442\u0430', blank=True)),
                ('image', models.FileField(null=True, upload_to=article.models.image_upload_to)),
                ('keys', models.CharField(max_length=1000, null=True, verbose_name='\u041a\u043b\u044e\u0447\u0438', blank=True)),
                ('published', models.BooleanField(default=False, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d')),
                ('author', models.ForeignKey(verbose_name='\u0410\u0432\u0442\u043e\u0440', blank=True, to='author.Profile', null=True)),
            ],
            options={
                'ordering': ['-date'],
                'db_table': 'article_article',
                'verbose_name': '\u0421\u0442\u0430\u0442\u044c\u044f',
                'verbose_name_plural': '\u0421\u0442\u0430\u0442\u044c\u0438',
            },
        ),
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=100, verbose_name='\u0412\u0430\u0448\u0435 \u0438\u043c\u044f')),
                ('text', models.TextField(verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('relation', models.ForeignKey(to='article.Article')),
            ],
            options={
                'db_table': 'article_comment',
                'verbose_name': '\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439',
                'verbose_name_plural': '\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('colour', models.CharField(max_length=50, null=True, verbose_name='\u0426\u0432\u0435\u0442')),
            ],
            options={
                'ordering': ['-name'],
                'db_table': 'categories',
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tags',
                'verbose_name': '\u0422\u0438\u043f',
                'verbose_name_plural': '\u0422\u0438\u043f',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', to='article.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ForeignKey(verbose_name='\u0422\u0438\u043f', to='article.Tag', null=True),
        ),
    ]
