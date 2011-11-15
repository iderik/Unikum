#!/usr/bin/env python

import os, sys
import pygame, world, sprites, entities, layer, render, view
from pygame.locals import *

# Game manager
class Game:
	def __init__(self, status=True):
		self.status = status
		self.mouse_pos = (0, 0)
		self.layers = [layer.TileLayer([[]], (32, 32))]
		self.view = view.View((640, 480))
		pygame.init()
		pygame.display.set_caption('Unikum 0.1')
		self.clock = pygame.time.Clock()
		self.window = pygame.display.set_mode((640, 480))
		self.sprites = sprites.Manager()
		self.world = world.Manager()
		self.load()
		self.update()

	# Load content
	def load(self):
		self.sprites.load('media/sprites.bmp')
		self.world.load(['data/world/layer0'])
		self.font = pygame.font.Font('freesansbold.ttf', 32)

	# Event triggers
	def events(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEBUTTONDOWN:
				if event.button in (1, 2, 3):
					pass	# left, middle or right
				elif event.button in (4, 5):
					pass	# scroll up or down
			elif event.type == MOUSEBUTTONUP:
				pass
			elif event.type == MOUSEMOTION:
				self.mouse_pos = event.pos
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.event.post(pygame.event.Event(QUIT))
			elif event.type == KEYUP:
				pass

	# Game loop
	def update(self):
		testsprite = pygame.transform.rotozoom(
				self.sprites.list[0][359], 0.0, 2.0)
		while self.status:
			self.window.fill(pygame.Color(0, 0, 0))		# Black background
			self.view.center_at((640-self.mouse_pos[0], 480-self.mouse_pos[1]))
			for layer in self.layers:
				render.render_tilelayer(self.window, layer, self.view, testsprite)
			self.events()
			pygame.display.update()						# Update display
			self.clock.tick(30)							# 30 FPS


# Main method
if __name__ == "__main__":
    game = Game()
