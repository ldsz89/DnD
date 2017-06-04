# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404,render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Character

# Create your views here.
def index(request):
    context = {}
    return render(request, 'ccreator/index.html', context)

class EditView(generic.DetailView):
    template_name = 'ccreator/edit.html'
    context_object_name = 'character'

class CharacterCreate(CreateView):
    model = Character
    fields = ['name', 'char_class', 'race', 'background', 'alignment',
    'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma',
    'acrobatics', 'animal_handling', 'arcana', 'athletics', 'deception', 'history',
        'insight', 'investigation', 'medicine', 'nature', 'perception', 'performance', 'persuasion', 'religion',
        'sleight_of_hand', 'stealth', 'survival']

class CharacterUpdate(UpdateView):
    model = Character
    fields = ['name', 'char_class', 'race', 'background', 'alignment',
    'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma',
    'acrobatics', 'animal_handling', 'arcana', 'athletics', 'deception', 'history',
        'insight', 'investigation', 'medicine', 'nature', 'perception', 'performance', 'persuasion', 'religion',
        'sleight_of_hand', 'stealth', 'survival']

class CharacterDelete(DeleteView):
    models = Character
    success_url = reverse_lazy('playermanager:characters')
