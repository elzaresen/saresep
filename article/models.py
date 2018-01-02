# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from author.models import *
from django.db import models
from redactor.fields import RedactorField
from datetime import datetime, timedelta
from django.template.defaultfilters import date


def image_upload_to(instance, filename):
    title = instance.title
    slug = slugify(title)
    basename, file_extension = filename.split(".")
    new_filename = "%s-%s.%s" % (slug, instance.id, file_extension)
    return "author/%s/%s" % (slug, new_filename)


def dead_date():
    return datetime.now() - timedelta(days=31)


class Tag(models.Model):
    class Meta:
        db_table = 'tags'
        verbose_name = u"Тип"
        verbose_name_plural = u"Тип"

    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    class Meta:
        db_table = 'categories'
        verbose_name = u"Категория"
        verbose_name_plural = u"Категории"
        ordering = ['slug', '-name']

    slug = models.IntegerField(null=True, blank=True, verbose_name='Место')
    name = models.CharField(max_length=100, verbose_name="Название")
    colour = models.CharField(max_length=50, null=True, verbose_name="Цвет")

    def __unicode__(self):
        return self.name

    def get_articles(self):
        return self.article_set.filter(published=True)[0:5]

    def get_news(self):
        return self.news_set.filter(date__gte=dead_date(), published=True)[0:8]

    def get_popular(self):
        return self.article_set.filter(date__gte=dead_date(), published=True).order_by('-rating')[0:3]


class Article(models.Model):
    class Meta:
        db_table = 'article_article'
        ordering = ['-date']
        verbose_name = u"Статья"
        verbose_name_plural = u"Статьи"

    title = models.CharField(max_length=1000, verbose_name='Заголовок')
    body = RedactorField(
        upload_to=image_upload_to,
        allow_file_upload=True,
        allow_image_upload=True,
        verbose_name='Текст')
    audio = models.FileField(upload_to=image_upload_to, null=True, blank=True)
    CART_CHOICES = (
        ('1', 'Биринчи'),
        ('2', 'Экинчи'),
        ('3', 'Үчүнчү'),
        ('4', 'Төртүнчү'),
        ('5', 'Бешинчи'),
    )
    cart = models.CharField(max_length=1, choices=CART_CHOICES, null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name='Категория')
    author = models.ForeignKey(Profile, verbose_name='Автор', null=True, blank=True)
    rate = models.IntegerField(default=0)
    view = models.IntegerField(default=0, verbose_name='Просмотры')
    rating = models.IntegerField(default=0)
    date = models.DateTimeField(null=True, verbose_name='Дата')
    image = models.FileField(upload_to=image_upload_to, null=True, blank=False)
    tag = models.ForeignKey(Tag, null=True, verbose_name="Тип")
    keys = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Ключи')
    published = models.BooleanField(blank=True, default=False, verbose_name='Опубликован')

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

    def get_text(self):
        return '%s...' % self.body[0:50]


class ArticleComment(models.Model):
    class Meta:
        db_table = 'article_comment'
        verbose_name = u"Комментарий"
        verbose_name_plural = u"Комментарии"

    author = models.CharField(max_length=100, verbose_name="Ваше имя")
    text = models.TextField(verbose_name="Комментарий")
    time = models.DateTimeField(auto_now_add=True)
    relation = models.ForeignKey(Article)

    @property
    def get_date(self):
        now = datetime.now()
        if date(now, 'Y/m/d') == date(self.time, 'Y/m/d'):
            return date(self.time + timedelta(hours=6), 'H:i:s')
        elif date(now - timedelta(days=1), 'Y/m/d') == date(self.time, 'Y/m/d'):
            return 'Кечээ - %s' % date(self.time + timedelta(hours=6), 'H:i:s')
        else:
            return date(self.time + timedelta(hours=6), 'Y/m/d - H:i:s')


class Ads(models.Model):
    class Meta:
        db_table = 'ads'
        verbose_name = u"Реклама"
        verbose_name_plural = u"Реклама"

    ADPOSITION = (
        ('1', 'Главная 1'),
        ('2', 'Главная 2'),
        ('3', 'Главная 3'),
        ('4', 'Главная 4'),
        ('5', 'Главная 5'),
        ('6', 'Главная 6'),
        ('7', 'Главная 7'),
        ('8', 'Главная 8'),
        ('9', 'Главная 9'),
        ('10', 'Главная 10'),
    )

    title = models.CharField(max_length=1000, verbose_name='Название')
    link = models.URLField(verbose_name="Ссылка")
    image = models.FileField(upload_to=image_upload_to, null=True, blank=False, verbose_name='Изображение')
    type = models.CharField(max_length=100, choices=ADPOSITION, null=True, verbose_name="Позиция")

    def __unicode__(self):
        return self.title