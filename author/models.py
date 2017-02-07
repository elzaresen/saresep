# -*- coding: utf-8 -*-
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.
def image_upload_to(instance, filename):
    title = instance.family
    slug = slugify(title)
    basename, file_extension = filename.split(".")
    new_filename = "%s-%s.%s" % (slug, instance.id, file_extension)
    return "author/%s/%s" % (slug, new_filename)


class Profile(models.Model):
    class Meta:
        verbose_name = u"Профиль"
        verbose_name_plural = u"Профили"

    family = models.ForeignKey(User, verbose_name="Пользователь", null=True, blank=True)
    avatar = models.ImageField(upload_to=image_upload_to, verbose_name="Фото")
    description = models.TextField(null=True, blank=True, verbose_name="Коротко о себе")
    facebook = models.CharField(max_length=1000, verbose_name="Профиль в Facebook", null=True, blank=True)
    googleplus = models.CharField(max_length=1000, verbose_name="Профиль в VK", null=True, blank=True)
    twitter = models.CharField(max_length=1000, verbose_name="Профиль в Twitter", null=True, blank=True)
    odnoklassniki = models.CharField(max_length=1000, verbose_name="Профиль в Одноклассниках", null=True, blank=True)

    def __unicode__(self):
        return '%s %s' % (self.family.first_name, self.family.last_name)
