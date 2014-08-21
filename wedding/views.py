from django.shortcuts import render, get_object_or_404, render_to_response
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

class InfoView(generic.ListView):
    model = Invitee
    template_name = 'wedding/info.html'

class KadotipsView(generic.ListView):
    model = Invitee
    template_name = 'wedding/kadotips.html'


class GuestsView(generic.ListView):
    template_name = 'wedding/guests.html'
    context_object_name = 'guest_list'

    def get_queryset(self):
        """Return the guests names"""
        return Invitee.objects.all().order_by('-party_name')[:5]

def vote(request, guest_id):
    p = get_object_or_404(Invitee, pk=guest_id)
    try:
        selected_choice = p.invitee_extra_set.get(pk=request.POST['choice'])
    except (KeyError, Invitee.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'wedding/detail.html', {
            'poll': p,
            'error_message': "You didn't select a attend.",
        })
    else:

        if selected_choice.test == '0':
            selected_choice.test = selected_choice
            selected_choice.save()
        else:
            selected_choice.test = 'pollo'
            selected_choice.save()


        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('wedding:detail', args=(p.id,)))

