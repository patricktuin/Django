from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
# Create your views here.
from food.models import Dish, Ingredient

class IndexView(generic.ListView):
    template_name = 'food/index.html'
    context_object_name = 'dish_list'

    def get_queryset(self):
        """Return all dishes"""
        return Dish.objects.order_by('name')[:5]

class DetailView(generic.DetailView):
    model = Dish
    template_name = 'food/detail.html'