#!/usr/bin/env python

import os
from layer import TileLayer, EntityLayer
from numpy import *

class Manager:
	def __init__(self):
		self.tilelayer = None
		self.transitionlayer = None
		self.entitylayer = None
		self.overlaylayer = None

		# For testing
		from entities import Entity_Player
		self.player = Entity_Player("Player", 100, (200, 200), (32, 32))


	def load(self, filepaths):
		for filepath in filepaths:
			if os.path.exists(filepath):
				stream = open(filepath, 'r')
				layer = [map(int, line.split(',')) for line in stream.readlines()]
				stream.close()
				self.tilelayer = TileLayer(array(layer), (32, 32))
				self.entitylayer = EntityLayer((640, 480))

				# For testing
				from entities import Entity_Creature
				self.entitylayer.add_entity(Entity_Creature("fisk", 1, (100, 100), (32, 32), None))
