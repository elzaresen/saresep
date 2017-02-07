# -*- coding: utf-8 -*-
from django.shortcuts import *
from django.core.context_processors import csrf
from datetime import datetime, timedelta
from .models import News, NewsComment, Category
from .forms import CommentFormNews
from django.core.paginator import Paginator
from operator import attrgetter
from article.models import Article
from itertools import chain


# Create your views here.

def main(request):
    hold = datetime.now() - timedelta(days=14)
    thershold = datetime.now() - timedelta(hours=24)
    args = {'categories': Category.objects.order_by('slug','name').exclude(name='Кумурзстан').exclude(name='RU'),
            "categories_nav": Category.objects.order_by('slug','name'),
            'news': News.objects.filter(published = True).order_by('-date')[0:15],
            'all_24': sorted(chain(News.objects.filter(published=True),
                                   Article.objects.filter(published = True)),
                             key=lambda instance: instance.date, reverse=True),
            # 'all_24': sorted(chain(News.objects.filter(date__gte=thershold,
            #                                            published=True),
            #                        Article.objects.filter(date__gte=thershold,
            #                                               published = True)),
            #                  key=lambda instance: instance.date, reverse=True),
            'popular_news': News.objects.filter(date__gte=thershold, published = True).order_by('-rating')[0:5],
            'viewed': News.objects.all().filter(date__gte=hold, published = True).order_by('-news_view')[0:15],
            'popular_articles': Article.objects.filter(
                date__gte=hold,published = True).order_by('-rating', '-date')[0:6],
            'category_name': 'гезитинин маалымат порталы'
            }
    try:
        aikol = Category.objects.get(name="Кумурзстан").id
        args['Kumurzstan'] = Article.objects.filter(category_id=aikol,published = True)[:6].reverse()
        args['aikol'] = Category.objects.get(id=aikol)
    except:
        pass
    try:
        args['a1'] = Article.objects.filter(cart='1',published = True).last()
    except:
        pass
    try:
        args['a2'] = Article.objects.filter(cart='2',published = True).last()
    except:
        pass
    try:
        args['a3'] = Article.objects.filter(cart='3',published = True).last()
    except:
        pass
    try:
        args['a4'] = Article.objects.filter(cart='4',published = True).last()
    except:
        pass
    return render(request, 'main.html', args)


def teaser(request):
    return render(request, 'teaser.html')


def kabar(request, news_id):
    args = {}
    threshold = datetime.now() - timedelta(hours=48)
    args.update(csrf(request))
    x = News.objects.get(id=news_id)
    x.view += 1
    x.save()
    x.rating = x.view + x.rate
    x.save()
    args = dict(novost=x, categories_nav=Category.objects.order_by('slug','name'),
                popular=News.objects.filter(date__gte=threshold,
                published = True).order_by('-rating').exclude(id=x.id)[0:5],
                # newest=News.objects.filter(category_id=x.category_id).filter(date__gte=threshold).order_by(
                #    '-view').exclude(id=x.id)[0:3],
                # by_category=Article.objects.filter(category_id=x.category_id).filter(date__gte=threshold)[0:3],
                comments=NewsComment.objects.filter(relation_id=news_id), form=CommentFormNews)
    return render(request, 'kabar.html', args)


def category(request, category_id, page_number):
    category_name = Category.objects.get(id=category_id)
    args = {}
    page_number = int(page_number)
    s = []
    for i in Article.objects.filter(category=category_name,published = True):
        s.append(i)
    for i in News.objects.filter(category=category_name,published = True):
        s.append(i)
    o = tuple(sorted(s, key=attrgetter('date'), reverse=True))
    current = o[15 * (page_number - 1):15 * page_number]
    a = o.__len__() // 15
    if o.__len__() % 15 == 0 and o.__len__() != 0:
        args['a'] = a + 1
    else:
        args['a'] = a + 2
    args['all'] = current
    args['next'] = page_number + 1
    args['previous'] = page_number - 1
    args['categories_nav'] = Category.objects.order_by('slug','name')
    args['category_name'] = category_name
    return render_to_response('category.html', args)


def addcomment(request, news_id):
    if request.POST:
        form = CommentFormNews(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.relation = News.objects.get(id=news_id)
            form.save()
            x = News.objects.get(id=news_id)
            x.rate = NewsComment.objects.filter(relation_id=news_id).count()
            x.save()
    return redirect('/news/%s/' % news_id)
