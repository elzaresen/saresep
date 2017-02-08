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
        "categories2": Category.objects.all()[0:8],
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
    args['last'] = Article.objects.filter(published=True, date__gte=threshold).order_by('-date', '-view')[0:4]
    args['categories'] = Category.objects.all()
    return render(request, 'main.html', args)


# def teaser(request):
#     return render(request, 'teaser.html')

def category(request, category_id, page_number):
    category_name = Category.objects.get(id=category_id)
    args = {}
    page_number = int(page_number)
    o = Article.objects.filter(category=category_name, published=True).order_by('-date')
    current = o[20 * (page_number - 1):20 * page_number]
    a = o.count() // 20
    if o.count() % 20 == 0 and o.count() != 0:
        args['a'] = a + 1
    else:
        args['a'] = a + 2
    args['current'] = current[0:4]
    args['all'] = current[4:20]
    args['next'] = page_number + 1
    args['previous'] = page_number - 1
    args['categories_nav'] = Category.objects.order_by('slug', 'name')
    args['active'] = category_name.name
    args['category_name'] = category_name
    args["categories2"] = Category.objects.all()[0:8]
    args["categories1"] = Category.objects.all()[8:16]
    return render_to_response('category.html', args)
