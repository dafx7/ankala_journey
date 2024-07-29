from django.urls import path
from .views import article_list, article

urlpatterns = [
    path('', article_list, name='article_list'),
    path('article', article, name='article'),
]
