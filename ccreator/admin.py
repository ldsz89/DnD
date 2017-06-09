# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Character, Feature, Trait, Language, Equipment, Spell

# Register your models here.
class FeatureInLine(admin.TabularInline):
    model = Feature
    extra = 1

class TraitsInLine(admin.TabularInline):
    model = Trait
    extra = 1

class LanguagesInLine(admin.TabularInline):
    model = Language
    extra = 1

class EquipmentInLine(admin.TabularInline):
    model = Equipment
    extra = 1

class SpellsInLine(admin.TabularInline):
    model = Spell
    extra = 1

class CharacterAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User', {'fields': ['user']}),
        ('Character Info', {'fields': ['name', 'char_class', 'race', 'background', 'alignment', 'level', 'avatar']}),
        ('Personality', {'fields': ['personality', 'ideals', 'bonds', 'flaws']}),
        ('Attributes', {'fields': ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']}),
        ('Skills', {'fields': ['acrobatics', 'animal_handling', 'arcana', 'athletics', 'deception', 'history',
            'insight', 'investigation', 'medicine', 'nature', 'perception', 'performance', 'persuasion', 'religion',
            'sleight_of_hand', 'stealth', 'survival']})
    ]
    inlines = [FeatureInLine, TraitsInLine, LanguagesInLine, EquipmentInLine, SpellsInLine]

admin.site.register(Character, CharacterAdmin)
