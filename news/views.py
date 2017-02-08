# -*- coding: utf-8 -*-
from django.shortcuts import *
from django.core.context_processors import csrf
from datetime import datetime, timedelta
from .models import Category
from django.core.paginator import Paginator
from operator import attrgetter
from article.models import Article
from itertools import chain


# Create your views here.

def main(request):
    args = {
        "categories_nav": Category.objects.order_by('slug', 'name')[0:7],
        "categories": Category.objects.all()[0:8],
        "categories1": Category.objects.all()[8:16]
    }
    try:
        args['a1'] = Article.objects.filter(cart='1', published=True).first()
    except:
        pass
    try:
        args['a2'] = Article.objects.filter(cart='2', published=True).first()
    except:
        pass
    try:
        args['a3'] = Article.objects.filter(cart='3', published=True).first()
    except:
        pass
    try:
        args['a4'] = Article.objects.filter(cart='4', published=True).first()
    except:
        pass
    try:
        args['a5'] = Article.objects.filter(cart='5', published=True).first()
    except:
        pass
    threshold = datetime.now() - timedelta(hours=24)
    args['last'] = Article.objects.filter(published=True, date__gte=threshold).order_by('-date','-view')[0:4]
    args['categories'] = Category.objects.all()
    return render(request, 'main.html', args)


def teaser(request):
    return render(request, 'teaser.html')


def category(request, category_id):
    category_name = Category.objects.get(id=category_id)
    args = {}
    return render_to_response('category.html', args)
