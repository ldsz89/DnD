# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import requests
import json

from .models import Character, Feature

# Create your views here.
class CharacterCreate(CreateView):
    model = Character
    fields = ['name', 'char_class', 'race', 'background', 'alignment', 'level',
    'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma',
    'acrobatics', 'animal_handling', 'arcana', 'athletics', 'deception', 'history',
        'insight', 'intimidation', 'investigation', 'medicine', 'nature', 'perception', 'performance', 'persuasion', 'religion',
        'sleight_of_hand', 'stealth', 'survival', 'avatar', 'user',
        'personality', 'ideals', 'bonds', 'flaws']

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        data = requests.get('http://dnd5eapi.co/api/classes/')
        classes = []
        for c in data.json()['results']:
            classes.append(c['name'])
        # context['classes'] = response['results']
        context['classes'] = classes
        return context

class CharacterUpdate(UpdateView):
    model = Character
    fields = ['name', 'char_class', 'race', 'background', 'alignment', 'level',
    'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma',
    'acrobatics', 'animal_handling', 'arcana', 'athletics', 'deception', 'history',
        'insight', 'intimidation', 'investigation', 'medicine', 'nature', 'perception', 'performance', 'persuasion', 'religion',
        'sleight_of_hand', 'stealth', 'survival', 'avatar', 'user',
        'personality', 'ideals', 'bonds', 'flaws']

# TO BE DELETED
class CharacterDelete(DeleteView):
    models = Character
    success_url = reverse_lazy('playermanager:characters')

class FeatureCreate(CreateView):
    models = Feature
    fields = ['name', 'description', 'character']

@login_required(login_url='/accounts/login/')
def character_delete(request, pk):
    character = get_object_or_404(Character, pk=pk)
    context = {
        'character': character
    }
    if request.method == "POST":
        current_user = request.user
        if character.user == current_user:
            name = character.name
            parent_obj_url = character.get_absolute_url()
            character.delete()
            # messages.success(request, name+" has been deleted.")
            return render(request, 'playermanager/characters.html', context)
        else:
            messages.error(request, 'This character can only be deleted by the owner')
    return render(request, 'ccreator/confirm_delete.html', context)
