# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from article.models import *


# Create your models here.
def image_upload_to(instance, filename):
    return "images/%s" % filename
