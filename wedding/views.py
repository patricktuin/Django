from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext, loader
# Create your views here.
from wedding.models import Invitee, Invitee_extra

class IndexView(generic.ListView):
    template_name = 'wedding/index.html'
    context_object_name = 'party_list'

    def get_queryset(self):
        """Return the party names"""
        return Invitee.objects.all().order_by('-party_name')[:5]

class DetailView(generic.DetailView):
    model = Invitee_extra
    template_name = 'wedding/detail.html'

def results(request, invitee_id):
    party_list = Invitee.objects.all().order_by('-party_name')[:5]
    context = {'party_list': party_list}
    return render(request, 'wedding/index.html', context)