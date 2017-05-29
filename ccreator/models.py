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
    strength = models.IntegerField(null=True)
    dexterity = models.IntegerField(null=True)
    constitution = models.IntegerField(null=True)
    intelligence = models.IntegerField(null=True)
    wisdom = models.IntegerField(null=True)
    charisma = models.IntegerField(null=True)
    acrobatics = models.IntegerField(null=True)
    animal_handling = models.IntegerField(null=True)
    arcana = models.IntegerField(null=True)
    athletics = models.IntegerField(null=True)
    deception = models.IntegerField(null=True)
    history = models.IntegerField(null=True)
    insight = models.IntegerField(null=True)
    intimidation = models.IntegerField(null=True)
    investigation = models.IntegerField(null=True)
    medicine = models.IntegerField(null=True)
    nature = models.IntegerField(null=True)
    perception = models.IntegerField(null=True)
    performance = models.IntegerField(null=True)
    persuasion = models.IntegerField(null=True)
    religion = models.IntegerField(null=True)
    sleight_of_hand = models.IntegerField(null=True)
    stealth = models.IntegerField(null=True)
    survival = models.IntegerField(null=True)
    armor_class = models.IntegerField(null=True)
    speed = models.IntegerField(null=True)
    hp = models.IntegerField(null=True)
    personality = models.IntegerField(null=True)
    ideals = models.IntegerField(null=True)
    bonds = models.IntegerField(null=True)
    flaws = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class CharacterFeatures(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Traits(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Languages(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Spells(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=250)

    def __str__(self):
        return self.name
