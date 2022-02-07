from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView

from news.models import News, Category
from .forms import NewsForm


class HomeNews(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'news/home_news_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новости'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class NewsByCategory(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'news/news_by_category.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True, category=self.kwargs['category_id'])

class ReadNews(DetailView):
    model = News
    template_name = 'news/read_news.html'
    context_object_name = 'news'

class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'

# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#
#     }
#     return render(request, template_name='news/index.html', context=context)
#
#
# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     context = {
#         'news': news,
#         'category': category,
#         'title': 'Список новостей',
#     }
#     return render(request, template_name='news/news_by_category.html', context=context)
#
#
# def read_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     context = {
#         'item': news_item,
#     }
#     return render(request, template_name='news/read_news.html', context=context)

# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form': form})
