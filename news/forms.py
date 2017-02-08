from django.forms import *
from .models import *


class CommentFormArticle(ModelForm):
    class Meta:
        model = ArticleComment
        fields = ['author','text']