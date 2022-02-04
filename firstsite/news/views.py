from django.shortcuts import render

from news.models import News, Category


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',

    }
    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category,
        'title': 'Список новостей',
    }
    return render(request, template_name='news/category.html', context=context)


def read_news(request, news_id):
    news_item = News.objects.get(pk=news_id)
    context = {
        'item': news_item,
    }
    return render(request, template_name='news/read_news.html', context=context)
