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
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()
    acrobatics = models.IntegerField()
    animal_handling = models.IntegerField()
    arcana = models.IntegerField()
    athletics = models.IntegerField()
    deception = models.IntegerField()
    history = models.IntegerField()
    insight = models.IntegerField()
    intimidation = models.IntegerField()
    investigation = models.IntegerField()
    medicine = models.IntegerField()
    nature = models.IntegerField()
    perception = models.IntegerField()
    performance = models.IntegerField()
    persuasion = models.IntegerField()
    religion = models.IntegerField()
    sleight_of_hand = models.IntegerField()
    stealth = models.IntegerField()
    survival = models.IntegerField()
    armor_class = models.IntegerField()
    speed = models.IntegerField()
    hp = models.IntegerField()
    personality = models.IntegerField()
    ideals = models.IntegerField()
    bonds = models.IntegerField()
    flaws = models.IntegerField()

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
