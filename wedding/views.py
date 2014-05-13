from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext, loader
# Create your views here.
from wedding.models import Invitee, Invitee_extra

class IndexView(generic.ListView):
    model = Invitee
    template_name = 'wedding/index.html'

class DetailView(generic.DetailView):
    model = Invitee
    template_name = 'wedding/detail.html'

class LocationView(generic.ListView):
    model = Invitee
    template_name = 'wedding/location.html'

class CeremoniemeesterView(generic.ListView):
    model = Invitee
    template_name = 'wedding/ceremoniemeester.html'

class FotosView(generic.ListView):
    model = Invitee
    template_name = 'wedding/fotos.html'

class OvernachtenView(generic.ListView):
    model = Invitee
    template_name = 'wedding/overnachten.html'

class KadotipsView(generic.ListView):
    model = Invitee
    template_name = 'wedding/kadotips.html'


class GuestsView(generic.ListView):
    template_name = 'wedding/guests.html'
    context_object_name = 'guest_list'

    def get_queryset(self):
        """Return the guests names"""
        return Invitee.objects.all().order_by('-party_name')[:5]





