#!/usr/bin/env python

import sys, os, pygame

# Sprite manager
class Manager:
	def __init__(self, sprite_width=16, sprite_height=16):
		self.sprite_width = sprite_width
		self.sprite_height = sprite_height
		self.list = []
		self.list_max = 0

	# Load sprites from a spritesheet.
	def load(self, filepath):
		sheet_image = pygame.image.load(filepath).convert_alpha()
		sheet_width, sheet_height = sheet_image.get_size()
		layer = []
		for sprite_y in range(0, sheet_height / self.sprite_height):
			for sprite_x in range(0, sheet_width / self.sprite_width):
				rect = (sprite_x * self.sprite_width, sprite_y * self.sprite_height, self.sprite_width, self.sprite_height)
				layer.append(sheet_image.subsurface(rect))
				self.list_max = self.list_max + 1
		self.list.append(layer)


