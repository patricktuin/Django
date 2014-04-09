from django.conf.urls import patterns, url

from food import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    (r'^search/$', views.search),
    #url(r'^search/$', views.search),
)
