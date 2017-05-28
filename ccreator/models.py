# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=250)
    char_class = models.CharField(max_length=50)
    race = models.CharField(max_length=50)
    background = models.CharField(max_length=50)
    alignment = models.CharField(max_length=50)
    strength = models.IntegerField(blank=True)
    dexterity = models.IntegerField(blank=True)
    constitution = models.IntegerField(blank=True)
    intelligence = models.IntegerField(blank=True)
    wisdom = models.IntegerField(blank=True)
    charisma = models.IntegerField(blank=True)
    acrobatics = models.IntegerField(blank=True)
    animal_handling = models.IntegerField(blank=True)
    arcana = models.IntegerField(blank=True)
    athletics = models.IntegerField(blank=True)
    deception = models.IntegerField(blank=True)
    history = models.IntegerField(blank=True)
    insight = models.IntegerField(blank=True)
    intimidation = models.IntegerField(blank=True)
    investigation = models.IntegerField(blank=True)
    medicine = models.IntegerField(blank=True)
    nature = models.IntegerField(blank=True)
    perception = models.IntegerField(blank=True)
    performance = models.IntegerField(blank=True)
    persuasion = models.IntegerField(blank=True)
    religion = models.IntegerField(blank=True)
    sleight_of_hand = models.IntegerField(blank=True)
    stealth = models.IntegerField(blank=True)
    survival = models.IntegerField(blank=True)
    armor_class = models.IntegerField(blank=True)
    speed = models.IntegerField(blank=True)
    hp = models.IntegerField(blank=True)
    personality = models.IntegerField(blank=True)
    ideals = models.IntegerField(blank=True)
    bonds = models.IntegerField(blank=True)
    flaws = models.IntegerField(blank=True)

class CharacterFeatures(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=250)

class Traits(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=250)

class Languages(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=250)

class Equipment(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=250)

class Spells(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
