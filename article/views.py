from django.shortcuts import render
from news.views import *
from datetime import datetime, timedelta
from news.forms import *


# Create your views here.


def article(request, article_id):
    args = {}
    args.update(csrf(request))
    x = Article.objects.get(id=article_id)
    x.view += 1
    x.save()
    x.rating = x.view + x.rate
    x.save()
    threshold = datetime.now() - timedelta(days=14)
    args = {
        "categories_nav": Category.objects.order_by('slug', 'name')[0:7],
        "categories": Category.objects.all()[0:8],
        "categories1": Category.objects.all()[8:16],
        'article': x,
        'by_category': Article.objects.filter(category_id=x.category_id,
                                              published=True,
                                              date__gte=threshold).order_by('-view').exclude(id=x.id)[0:4]
    }
    return render(request, 'article.html', args)


def addcomment(request, article_id):
    if request.POST:
        form = CommentFormArticle(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.relation = Article.objects.get(id=article_id)
            form.save()
            y = Article.objects.get(id=article_id)
            y.rate = ArticleComment.objects.filter(relation_id=article_id).count()
            y.save()
    return redirect('/article/%s/#comments' % article_id)
