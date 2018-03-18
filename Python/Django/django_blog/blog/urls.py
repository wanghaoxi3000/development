from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^page/(?P<page>[0-9]+)$', views.BlogList.as_view(), name='index'),
    url(r'^(?P<show>[A-Za-z]+)/(?P<name>[A-Za-z0-9\-_]+)/(?P<page>[0-9]+)$', views.BlogList.as_view(), name='filter'),
    url(r'^article/(?P<pk>[0-9]+)$', views.ArticleDetail.as_view(), name='article_detail'),
]
