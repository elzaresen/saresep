# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import author.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.ImageField(upload_to=author.models.image_upload_to, verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe')),
                ('description', models.TextField(null=True, verbose_name=b'\xd0\x9a\xd0\xbe\xd1\x80\xd0\xbe\xd1\x82\xd0\xba\xd0\xbe \xd0\xbe \xd1\x81\xd0\xb5\xd0\xb1\xd0\xb5', blank=True)),
                ('facebook', models.CharField(max_length=1000, null=True, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xbe\xd1\x84\xd0\xb8\xd0\xbb\xd1\x8c \xd0\xb2 Facebook', blank=True)),
                ('googleplus', models.CharField(max_length=1000, null=True, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xbe\xd1\x84\xd0\xb8\xd0\xbb\xd1\x8c \xd0\xb2 VK', blank=True)),
                ('twitter', models.CharField(max_length=1000, null=True, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xbe\xd1\x84\xd0\xb8\xd0\xbb\xd1\x8c \xd0\xb2 Twitter', blank=True)),
                ('odnoklassniki', models.CharField(max_length=1000, null=True, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xbe\xd1\x84\xd0\xb8\xd0\xbb\xd1\x8c \xd0\xb2 \xd0\x9e\xd0\xb4\xd0\xbd\xd0\xbe\xd0\xba\xd0\xbb\xd0\xb0\xd1\x81\xd1\x81\xd0\xbd\xd0\xb8\xd0\xba\xd0\xb0\xd1\x85', blank=True)),
                ('family', models.ForeignKey(verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u041f\u0440\u043e\u0444\u0438\u043b\u044c',
                'verbose_name_plural': '\u041f\u0440\u043e\u0444\u0438\u043b\u0438',
            },
        ),
    ]
