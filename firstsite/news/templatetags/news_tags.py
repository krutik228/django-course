from django import template

from news.models import Category

from django.db.models.aggregates import *

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.filter(news__is_published=True).distinct()


# @register.inclusion_tag('news/list_categories.html')
# def show_categories():
#     categories = Category.objects.all()
#     return {"categories:": categories}
