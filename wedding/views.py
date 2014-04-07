from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext, loader
# Create your views here.
from wedding.models import Invitee, Invitee_extra

def index(request):
    party_list = Invitee.objects.all().order_by('-party_name')[:5]
    context = {'party_list': party_list}
    return render(request, 'wedding/index.html', context)

def detail(request, invitee_id):
    question = get_object_or_404(Invitee, pk=invitee_id)
    return render(request, 'wedding/detail.html', {'party_name': party_name})