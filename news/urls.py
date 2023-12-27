from django.urls import path
from .views import makeNewNews, publishedNews


urlpatterns = [
    path('make/', makeNewNews.as_view()),
    path('list/', publishedNews.as_view()),
]