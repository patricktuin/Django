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
    model = Invitee
    template_name = 'wedding/detail.html'

class ResultsView(generic.DetailView):
    model = Invitee
    template_name = 'wedding/results.html'

def vote(request, invitee_id):
    p = get_object_or_404(Invitee, pk=invitee_id)
    try:
        selected_choice = p.invitee_extra_set.get(pk=request.POST['attend'])
    except (KeyError, Invitee.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'wedding/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.attend = 1 #+= 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('wedding:results', args=(p.id,)))