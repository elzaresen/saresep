# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *


class VideoAdmin(admin.ModelAdmin):
    list_display = '__unicode__ title url'.split()

admin.site.register(Video,VideoAdmin)