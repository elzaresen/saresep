# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from article.models import *
from django.db import models
from redactor.fields import RedactorField
from datetime import datetime, timedelta
from django.template.defaultfilters import date


# Create your models here.
def image_upload_to(instance, filename):
    title = instance.family
    slug = slugify(title)
    basename, file_extension = filename.split(".")
    new_filename = "%s-%s.%s" % (slug, instance.id, file_extension)
    return "author/%s/%s" % (slug, new_filename)


class News(models.Model):
    class Meta:
        db_table = 'news'
        ordering = ['-date']
        verbose_name = u"Новость"
        verbose_name_plural = u"Новости"

    title = models.CharField(max_length=1000, verbose_name='Заголовок')
    body = RedactorField(
        upload_to=image_upload_to,
        allow_file_upload=True,
        allow_image_upload=True,
        verbose_name='Текст')
    audio = models.FileField(upload_to=image_upload_to,null=True,blank=True)
    category = models.ForeignKey(Category, verbose_name='Категория')
    view = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)
    date = models.DateTimeField(blank=True,null=True, verbose_name='Дата')
    keys = models.CharField(max_length=1000,blank=True,null=True,verbose_name='Ключи')
    published = models.BooleanField(blank=True,default=False,verbose_name='Опубликован')

    def __unicode__(self):
        return self.title

    def get_date(self):
        now = datetime.now()
        if date(now, 'Y/m/d') == date(self.date, 'Y/m/d'):
            return date(self.date + timedelta(hours=6), 'H:i')
        elif date(now - timedelta(days=1), 'Y/m/d') == date(self.date, 'Y/m/d'):
            return 'Кечээ - %s' % date(self.date + timedelta(hours=6), 'H:i')
        elif date(now - timedelta(days=365), 'Y/m/d') == date(self.date, 'Y/m/d'):
            return date(self.date, 'Y/b/d')
        else:
            return date(self.date, 'd b')


class NewsComment(models.Model):
    class Meta:
        db_table = 'news_comment'
        verbose_name = u"Комментарий"
        verbose_name_plural = u"Комментарии"

    author = models.CharField(max_length=100, verbose_name="Ваше имя")
    text = models.TextField(verbose_name="Комментарий")
    time = models.DateTimeField(auto_now_add=True)
    relation = models.ForeignKey(News)

    def get_date(self):
        now = datetime.now()
        if date(now, 'Y/m/d') == date(self.time, 'Y/m/d'):
            return date(self.time + timedelta(hours=6), 'H:i:s')
        elif date(now - timedelta(days=1), 'Y/m/d') == date(self.time, 'Y/m/d'):
            return 'Кечээ - %s' % date(self.time + timedelta(hours=6), 'H:i:s')
        else:
            return date(self.time + timedelta(hours=6), 'Y/m/d - H:i:s')
