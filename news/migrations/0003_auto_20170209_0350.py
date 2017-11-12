# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_audio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='category',
        ),
        migrations.RemoveField(
            model_name='newscomment',
            name='relation',
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.DeleteModel(
            name='NewsComment',
        ),
    ]
