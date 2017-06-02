# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404,render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
    fields = ['name', 'background', 'alignment', 'char_class']
