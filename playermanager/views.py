# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django. contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views.generic import View
from django import forms

from ccreator.models import Character, Feature, Trait, Language, Equipment, Spell
from .forms import UserForm, UserLoginForm

# @login_required(login_url='/accounts/login/')
class DashboardView(generic.ListView):
    template_name = 'playermanager/dashboard.html'
    context_object_name = 'characters'

    def get_queryset(self):
        return Character.objects.all()

# @login_required(login_url='/accounts/login/')
# TO BE DELETED
class CharacterView(generic.ListView):
    template_name = 'playermanager/characters.html'
    context_object_name = 'characters'

    def get_queryset(self):
        return Character.objects.all()

@login_required(login_url='/accounts/login/')
def character_view(request):
    current_user = request.user
    characters = Character.objects.filter(user__exact=current_user.id)
    context = {
        'characters': characters,
    }
    return render(request, 'playermanager/characters.html', context)

class DetailView(generic.DetailView):
    model = Character
    template_name = 'playermanager/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['features'] = Feature.objects.filter(character__exact=self.kwargs['pk'])
        context['traits'] = Trait.objects.filter(character__exact=self.kwargs['pk'])
        context['languages'] = Language.objects.filter(character__exact=self.kwargs['pk'])
        context['equipment'] = Equipment.objects.filter(character__exact=self.kwargs['pk'])
        context['spells'] = Spell.objects.filter(character__exact=self.kwargs['pk'])
        return context

class UserFormView(View):
    form_class = UserForm
    template_name = 'playermanager/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # saves what the user inputs so we can do things with it. DOES NOT save info to the database
            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            # this line saves to the database
            user.save()

            # returns User objects if creditials are correct
            user = authenticate(username = username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('playermanager:dashboard')

        return render(request, self.template_name, {'form': form})
