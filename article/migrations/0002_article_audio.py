# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import article.models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='audio',
            field=models.FileField(null=True, upload_to=article.models.image_upload_to, blank=True),
        ),
    ]
