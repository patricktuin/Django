from django.conf.urls import patterns, url

from wedding import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^location/$', views.LocationView.as_view(), name='location'),
    url(r'^guests/$', views.GuestsView.as_view(), name='guests'),
	#url(r'^guests/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
)