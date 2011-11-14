#!/usr/bin/env python

import sys, os, fileio

# Entity manager
class Manager:
	def __init__(self):
		self.entity_list = []
		self.load()

	def load(self):
		file_stream = fileio.Stream()
		spawns = file_stream.parser.JSON_decode(file_stream.read("data/world/spawns"))
		templates = file_stream.parser.JSON_decode(file_stream.read("data/creatures"))
		for spawn in spawns:
			for template in templates:
				if spawn["name"] == template["name"]:
					entity_list.append(Entity_Creature(template["name"], template["sprite"], 
										(spawn["position_x"], spawn["position_y"]),
										(template["width"], template["height"])))
			break

	def delete(self, entity_id):
		if entity_id in self.entity_list:
			del self.entity_list[entity_id]

	# This can only handle X-axis and positive numbers. Fix this for Y-axis, negative numbers and diagonally!
	def entities_in_range(self, position, distance):
		return [(entity.rect[0], entity.rect[1]) for entity in self.entity_list if entity.rect[0] - distance]



class Entity:
	def __init__(self):
		self.name = ""
		self.sprite_id = 0
		self.rect = (0, 0, 0, 0)

	def move(self, direction, velocity):
		pass

	def attack(self, entity):
		pass



class Entity_Creature(Entity):
	def __init__(self, name, sprite_id, position, size, interval):
		self.name = name
		self.sprite_id = sprite_id
		self.rect = (position[0], position[1], size[0], size[1])



# Player object
class Entity_Player(Entity):
	def __init__(self, name, sprite_id, position, size):
		self.name = name
		self.sprite_id = sprite_id
		self.rect = (position[0], position[1], size[0], size[1])

