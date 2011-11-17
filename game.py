#!/usr/bin/env python

import os, sys
import pygame, world, sprites, entities, render, view
from pygame.locals import *

# Game manager
class Game:
	def __init__(self, status=True):
		self.status = status
		self.mouse_pos = (0, 0)
		self.view = view.View((640, 480))
		pygame.init()
		pygame.display.set_caption('Unikum 0.1')
		self.clock = pygame.time.Clock()
		self.window = pygame.display.set_mode((640, 480))
		self.sprites = sprites.Manager()
		self.world = world.Manager()
		self.keys = []
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
				self.keys.append(event.key)
			elif event.type == KEYUP:
				self.keys.remove(event.key)
	# Game loop
	def update(self):
		while self.status:
			self.window.fill(pygame.Color(0, 0, 0))		# Black background
			self.view.center_at((self.world.player.rect[0], self.world.player.rect[1]))

			# For testing
			if K_a in self.keys:
				self.world.player.rect = (self.world.player.rect[0]-10, self.world.player.rect[1], self.world.player.rect[2], self.world.player.rect[3])
			if K_d in self.keys:
				self.world.player.rect = (self.world.player.rect[0]+10, self.world.player.rect[1], self.world.player.rect[2], self.world.player.rect[3])
			if K_w in self.keys:
				self.world.player.rect = (self.world.player.rect[0], self.world.player.rect[1]-10, self.world.player.rect[2], self.world.player.rect[3])
			if K_s in self.keys:
				self.world.player.rect = (self.world.player.rect[0], self.world.player.rect[1]+10, self.world.player.rect[2], self.world.player.rect[3])

			render.draw_world(self.window, self.world, self.view, self.sprites.list[0])

			self.events()
			pygame.display.update()						# Update display
			self.clock.tick(30)							# 30 FPS


# Main method
if __name__ == "__main__":
    game = Game()
