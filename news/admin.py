from django.contrib import admin
from .models import NewsComment,News
# Register your models here.


class NewsInline(admin.StackedInline):
    model = NewsComment
    fields = ['author','text']
    extra = 1


class NewsAdmin(admin.ModelAdmin):
    fields = 'title date body audio published keys category'.split()
    list_filter = 'category published date'.split()
    list_display = '__unicode__ published date category'.split()
    list_per_page = 20
    list_editable = 'category'.split()
    inlines = [NewsInline]


admin.site.register(News, NewsAdmin)