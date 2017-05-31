# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import Http404
from ccreator.models import Character

# Create your views here.

def dashboard(request):
    characters = Character.objects.all()
    context = {
        'characters': characters
    }
    return render(request, 'playermanager/dashboard.html', context)

def characters(request):
    characters = Character.objects.all()
    context = {
        'characters': characters
    }
    return render(request, 'playermanager/characters.html', context)

def detail(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    return render(request, 'playermanager/detail.html', {'character': character})

    # try:
    #     character = Character.objects.get(pk=character_id)
    # except Character.DoesNotExist:
    #     raise Http404("Character does not exist")
    # return render(request, 'playermanager/detail.html', {'character': character})
