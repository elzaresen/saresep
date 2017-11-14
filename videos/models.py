# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from urlparse import urlparse, parse_qs

import re
from django.db import models
from author.models import *
from django.db import models
from redactor.fields import RedactorField
from datetime import datetime, timedelta
from django.template.defaultfilters import date
# Create your models here.
class Video(models.Model):
    class Meta:
        db_table = 'videos'
        ordering = ['-date']
        verbose_name = u"Видео"
        verbose_name_plural = u"Видеолор"

    title = models.CharField(max_length=1000, verbose_name='Заголовок')
    url = models.CharField(max_length=20, verbose_name='Ссылка')
    date = models.DateTimeField(null=True, verbose_name='Дата')
    def __unicode__(self):
        return self.title
