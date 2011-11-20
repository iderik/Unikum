#!/usr/bin/env python

import os
import vector
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

				self.transitionlayer = generate_transitions(self.tilelayer)

# Brute force transition generation
def generate_transitions(tilelayer):
	TOP = 1
	BOTTOM = 6
	LEFT = 3
	RIGHT = 4

	TOPLEFT = 0
	TOPRIGHT = 2
	BOTTOMLEFT = 5
	BOTTOMRIGHT = 7
	transitionlayer = TileLayer(fill(40, tilelayer.size), (32, 32))
	for y in range(transitionlayer.size[1]):
		for x in range(transitionlayer.size[0]):
			tile_id = tilelayer.get_tile((x, y))
			if tile_id == 20:
				table = [tilelayer.get_tile(vector.add((x, y), v)) == 0 for v in [(-1, -1), (0, -1), (1, -1), \
						(-1, 0),         (1, 0), \
						(-1, 1), (0, 1), (1, 1)] ]

				t = transitionlayer.get_tile((x, y))

				# Very ugly but suitable for testing
				if table[LEFT] and table[RIGHT] and table[TOP] and table[BOTTOM]:
					t = 15
				elif table[LEFT] and table[RIGHT] and table[TOP]:
					t = 7
				elif table[LEFT] and table[TOP] and table[BOTTOM]:
					t = 11
				elif table[LEFT] and table[RIGHT]:
					t = 5
				elif table[LEFT] and table[TOP]:
					t = 3
				elif table[LEFT] and table[BOTTOM]:
					t = 9
				elif table[LEFT]:
					t = 1
				elif table[RIGHT] and table[TOP] and table[BOTTOM]:
					t = 14
				elif table[RIGHT] and table[TOP]:
					t = 6
				elif table[RIGHT] and table[BOTTOM]:
					t = 12
				elif table[RIGHT]:
					t = 4
				elif table[TOP] and table[BOTTOM]:
					t = 10
				elif table[TOP]:
					t = 2
				elif table[BOTTOM]:
					t = 8

				transitionlayer.set_tile((x, y), t)
				
	return transitionlayer

def fill(n, size):
	rows = []
	for y in range(size[1]):
		rows.append([n for x in range(size[0])])
	return array(rows)
