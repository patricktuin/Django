from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.core import serializers

# Create your views here.
from food.models import Dish, Ingredient
import json

class IndexView(generic.ListView):
    template_name = 'food/index.html'
    context_object_name = 'dish_list'

    def get_queryset(self):
        """Return all dishes"""
        return Dish.objects.order_by('name')[:5]

class DetailView(generic.DetailView):
    model = Dish
    template_name = 'food/detail.html'

class SearchView(generic.ListView):
    model = Dish
    template_name = 'food/search.html'

#Work in progress!!!!!!
def search(request):
    search = request.GET['q']
    if search != '':
        message = Dish.objects.filter(name__contains=search)
        #message = 'You searched for: %s' %request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)

def myjson(request):
    data = Dish.objects.all()
    #data = {'string':'test', 'twee':'pollo'}
    #data = serializers.serialize('json', data)
    data = json.dumps( [{'name': o.name, 'description': o.description, 'persons': o.persons} for o in data])
    return HttpResponse(json.dumps(data),mimetype="application/json")