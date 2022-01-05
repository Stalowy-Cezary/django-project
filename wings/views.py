from django.utils.text import slugify
from django.shortcuts import render
from .models import Boss, Raid
from django.views import generic
from django.http import HttpResponse


class HomeListView(generic.ListView):
    model = Raid
    template_name = 'base_generic.html'

class RaidListView(HomeListView):

    template_name = 'raid_list.html'




