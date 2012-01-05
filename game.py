#!/usr/bin/env python

import os, sys
import pygame, world, sprites, entities, render, view, vector, engine, hud
from pygame.locals import *

# Game manager
class Game:
	def __init__(self, status=True):
		# Pygame
		pygame.init()
		pygame.display.set_caption('Unikum 0.1')

		# General
		self.clock = pygame.time.Clock()
		self.status = status
		self.tile_size = (32, 32)
		self.view = view.View((10, 10, self.tile_size[0] * 20, self.tile_size[1] * 15))
		self.mouse_pos = (0, 0)
		self.keys = set()

		# Main surface (display)
		self.window_resolution = (800, 600)
		self.window_flag = pygame.FULLSCREEN
		self.window_depth = 0	# FIXME
		self.window = pygame.display.set_mode(self.window_resolution, self.window_flag, self.window_depth)

		# Managers
		self.world = world.Manager()
		self.sprites = sprites.Manager()
		self.hud = hud.Hud(self.window_resolution, self.view.rect)

		# Process
		self.load()
		self.update()

	# Load content
	def load(self):
		self.sprites.load('media/sprites.bmp')
		self.sprites.load('media/terrain.png')
		self.world.load(['data/world/layer0'])
		self.hud.load(filepath_sheet="media/hud2.png", filepath_cfg="data/hud")
		self.font = pygame.font.Font('freesansbold.ttf', 32)

	# Event actions
	def events(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEBUTTONDOWN:
				if event.button in (1, 2, 3):	# left, middle or right
					pass	
				elif event.button in (4, 5):	# scroll up or down
					pass
			elif event.type == MOUSEBUTTONUP:
				pass
			elif event.type == MOUSEMOTION:
				self.mouse_pos = event.pos
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.event.post(pygame.event.Event(QUIT))
				self.keys.add(event.key)
			elif event.type == KEYUP:
				self.keys.discard(event.key)

	# Game loop
	def update(self):
		while self.status:
			self.window.fill(pygame.Color(0, 0, 0))		# Black background
			self.view.center_at(self.world.player.position)

			# World
			engine.update_world(self.world, self.keys, 1/30.0)
			render.draw_world(self.window, self.world, self.view, self.sprites.list)

			# HUD
			engine.update_hud(self.hud, self.world)
			render.draw_hud(self.window, self.hud)

			# Events
			self.events()

			# Update surface (window), 30 FPS.
			pygame.display.update()
			self.clock.tick(30)



# Main
if __name__ == "__main__":
    game = Game()
