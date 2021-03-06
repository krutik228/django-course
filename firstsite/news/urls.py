# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    # path('', index, name='home'),
    # path('', cache_page(60)(HomeNews.as_view()), name='home'),  # cashed HomePage
    path('', HomeNews.as_view(), name='home'),
    # path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('read_news/<int:pk>/', ReadNews.as_view(), name='read_news'),
    # path('read_news/<int:pk>/', read_news, name='read_news'),
    path('add_news/', CreateNews.as_view(), name='add_news'),
    # path('add_news/', add_news, name='add_news'),
]
