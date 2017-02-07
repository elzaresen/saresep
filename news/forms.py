from django.forms import *
from .models import *


class CommentFormNews(ModelForm):
    class Meta:
        model = NewsComment
        fields = ['author','text']


class CommentFormArticle(ModelForm):
    class Meta:
        model = ArticleComment
        fields = ['author','text']