from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
# Create your views here.
from wedding.models import Invitee, Invitee_extra

class IndexView(generic.ListView):
    template_name = 'wedding/index.html'
    context_object_name = 'invitee_list'

    def get_queryset(self):
        """Return all Invitee's"""
        return Invitee.objects.order_by('party_name')

class DetailView(generic.DetailView):
    model = Invitee
    template_name = 'wedding/detail.html'