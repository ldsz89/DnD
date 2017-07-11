# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from dnd import settings
import os
from django.contrib.auth.models import User

# Create your models here.

class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    char_class = models.CharField(max_length=50, null=True, blank=True)
    race = models.CharField(max_length=50, null=True, blank=True)
    background = models.CharField(max_length=50, null=True, blank=True)
    alignment = models.CharField(max_length=50, null=True, blank=True)
    level = models.IntegerField(null=True, blank=True,default=1)
    strength = models.IntegerField(null=True, blank=True,default=1)
    dexterity = models.IntegerField(null=True, blank=True,default=1)
    constitution = models.IntegerField(null=True, blank=True,default=1)
    intelligence = models.IntegerField(null=True, blank=True,default=1)
    wisdom = models.IntegerField(null=True, blank=True,default=1)
    charisma = models.IntegerField(null=True, blank=True,default=1)
    acrobatics = models.IntegerField(null=True, blank=True,default=0)
    acrobatics_prof = models.BooleanField(default=False)
    animal_handling = models.IntegerField(null=True, blank=True,default=0)
    arcana = models.IntegerField(null=True, blank=True,default=0)
    athletics = models.IntegerField(null=True, blank=True,default=0)
    deception = models.IntegerField(null=True, blank=True,default=0)
    history = models.IntegerField(null=True, blank=True,default=0)
    insight = models.IntegerField(null=True, blank=True,default=0)
    intimidation = models.IntegerField(null=True, blank=True,default=0)
    investigation = models.IntegerField(null=True, blank=True,default=0)
    medicine = models.IntegerField(null=True, blank=True,default=0)
    nature = models.IntegerField(null=True, blank=True,default=0)
    perception = models.IntegerField(null=True, blank=True,default=0)
    performance = models.IntegerField(null=True, blank=True,default=0)
    persuasion = models.IntegerField(null=True, blank=True,default=0)
    religion = models.IntegerField(null=True, blank=True,default=0)
    sleight_of_hand = models.IntegerField(null=True, blank=True,default=0)
    stealth = models.IntegerField(null=True, blank=True,default=0)
    survival = models.IntegerField(null=True, blank=True,default=0)
    armor_class = models.IntegerField(null=True, blank=True)
    speed = models.IntegerField(null=True, blank=True)
    hp = models.IntegerField(null=True, blank=True)
    personality = models.CharField(max_length=250, null=True, blank=True)
    ideals = models.CharField(max_length=250, null=True, blank=True)
    bonds = models.CharField(max_length=250, null=True, blank=True)
    flaws = models.CharField(max_length=250, null=True, blank=True)
    avatar = models.FileField(null=True, blank=True, default=None)

    def get_absolute_url(self):
        return reverse('playermanager:detail', kwargs={'pk': self.pk})

    def delete(self):
        if self.avatar.name:
            # os.remove(settings.MEDIA_ROOT+self.avatar.path)
            os.remove(self.avatar.path)
        return super(Character, self).delete()

    def __str__(self):
        return self.name

class Feature(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    url = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

class Trait(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    url = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    url = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    url = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

class Spell(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    url = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name
