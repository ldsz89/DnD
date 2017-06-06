# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ccreator.models import Character, Feature, Trait, Language, Equipment, Spell

# Create your views here.

class DashboardView(generic.ListView):
    template_name = 'playermanager/dashboard.html'
    context_object_name = 'characters'

    def get_queryset(self):
        return Character.objects.all()

class CharacterView(generic.ListView):
    template_name = 'playermanager/characters.html'
    context_object_name = 'characters'

    def get_queryset(self):
        return Character.objects.all()

class DetailView(generic.DetailView):
    model = Character
    template_name = 'playermanager/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        # context['features'] = CharacterFeatures.objects.filter(character__exact=super(DetailView, self).model)
        context['features'] = Feature.objects.filter(character__exact=self.kwargs['pk'])
        context['traits'] = Trait.objects.filter(character__exact=self.kwargs['pk'])
        context['languages'] = Language.objects.filter(character__exact=self.kwargs['pk'])
        context['equipment'] = Equipment.objects.filter(character__exact=self.kwargs['pk'])
        context['spells'] = Spell.objects.filter(character__exact=self.kwargs['pk'])
        return context
