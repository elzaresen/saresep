# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import news.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='audio',
            field=models.FileField(null=True, upload_to=news.models.image_upload_to, blank=True),
        ),
    ]
