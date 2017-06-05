# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=250)
    char_class = models.CharField(max_length=50, null=True, blank=True)
    race = models.CharField(max_length=50, null=True, blank=True)
    background = models.CharField(max_length=50, null=True, blank=True)
    alignment = models.CharField(max_length=50, null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    strength = models.IntegerField(null=True, blank=True)
    dexterity = models.IntegerField(null=True, blank=True)
    constitution = models.IntegerField(null=True, blank=True)
    intelligence = models.IntegerField(null=True, blank=True)
    wisdom = models.IntegerField(null=True, blank=True)
    charisma = models.IntegerField(null=True, blank=True)
    acrobatics = models.IntegerField(null=True, blank=True)
    animal_handling = models.IntegerField(null=True, blank=True)
    arcana = models.IntegerField(null=True, blank=True)
    athletics = models.IntegerField(null=True, blank=True)
    deception = models.IntegerField(null=True, blank=True)
    history = models.IntegerField(null=True, blank=True)
    insight = models.IntegerField(null=True, blank=True)
    intimidation = models.IntegerField(null=True, blank=True)
    investigation = models.IntegerField(null=True, blank=True)
    medicine = models.IntegerField(null=True, blank=True)
    nature = models.IntegerField(null=True, blank=True)
    perception = models.IntegerField(null=True, blank=True)
    performance = models.IntegerField(null=True, blank=True)
    persuasion = models.IntegerField(null=True, blank=True)
    religion = models.IntegerField(null=True, blank=True)
    sleight_of_hand = models.IntegerField(null=True, blank=True)
    stealth = models.IntegerField(null=True, blank=True)
    survival = models.IntegerField(null=True, blank=True)
    armor_class = models.IntegerField(null=True, blank=True)
    speed = models.IntegerField(null=True, blank=True)
    hp = models.IntegerField(null=True, blank=True)
    personality = models.CharField(max_length=250, null=True, blank=True)
    ideals = models.CharField(max_length=250, null=True, blank=True)
    bonds = models.CharField(max_length=250, null=True, blank=True)
    flaws = models.CharField(max_length=250, null=True, blank=True)
    avatar = models.FileField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('playermanager:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

class CharacterFeatures(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

class Traits(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

class Languages(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

class Spells(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name
