from django.conf.urls import patterns, url

from wedding import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^location/$', views.LocationView.as_view(), name='location'),
    url(r'^ceremoniemeester/$', views.CeremoniemeesterView.as_view(), name='ceremoniemeester'),
    url(r'^fotos/$', views.FotosView.as_view(), name='fotos'),
    url(r'^overnachten/$', views.OvernachtenView.as_view(), name='overnachten'),
    url(r'^kadotips/$', views.KadotipsView.as_view(), name='kadotips'),
    url(r'^guests/$', views.GuestsView.as_view(), name='guests'),
	url(r'^guests/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
)