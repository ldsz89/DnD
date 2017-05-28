# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from ccreator.models import Character

# Create your views here.

def dashboard(request):
    characters = Character.objects.all()
    context = {
        'characters': characters
    }
    return render(request, 'playermanager/dashboard.html', context)
