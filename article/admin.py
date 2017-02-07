# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = '__unicode__ name slug'.split()
    list_editable = 'slug'.split()

admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag)


class ArticleInline(admin.StackedInline):
    model = ArticleComment
    fields = ['author','text']
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    fields = 'title date cart body audio image keys published category tag author'.split()
    list_display = '__unicode__ published cart date view category author'.split()
    list_per_page = 20
    list_filter = 'date category published author'.split()
    list_editable = 'cart category'.split()
    inlines = [ArticleInline]


admin.site.register(Article, ArticleAdmin)
