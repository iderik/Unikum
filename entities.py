#!/usr/bin/env python

import sys, os, simplejson

# Entity manager
class Manager:
	def __init__(self):
		pass

# Entity baseobject
class Entity:
	def __init__(self):
		self.rect = (0, 0, 0, 0)
		self.sprite_id = []

# Tile object
class Entity_Tile(Entity):
	def __init__(self):
		pass

# Item object
class Entity_Item(Entity):
	def __init_(self):
		pass

# Living baseobject
class Entity_Living(Entity):
	def __init__(self):
		self.name = None

	def move(self, direction, velocity):
		pass

	def attack(self, entity_living):
		pass	# Check inCamera, range, strength, weapon, armor, health

# Creature object
class Entity_Creature(Entity_Living):
	def __init__(self, name):
		pass

# NPC object
class Entity_NPC(Entity_Living):
	def __init__(self):
		pass

# Player object
class Entity_Player(Entity_Living):
	def __init__(self, name, sprite_id, position, size):
		self.name = name
		self.sprite_id = sprite_id
		self.rect = (position[0], position[1], size[0], size[1])
