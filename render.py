from view import View
import vector

import pygame
from pygame.locals import *

def draw_world(surface, world, view, tileset):
	draw_tilelayer(surface, world.tilelayer, view, tileset)
	draw_entitylayer(surface, world.entitylayer, view, tileset)
	draw_player(surface, world.player, view, tileset)

def draw_tilelayer(surface, tilelayer, view, tileset):
	for y in range(tilelayer.size[1]):
		for x in range(tilelayer.size[0]):
			screenpos = view.transform((tilelayer.tilesize[0]*x, tilelayer.tilesize[1]*y))
			tile = pygame.transform.rotozoom(tileset[tilelayer.get_tile((x, y))], 0.0, 2.0)
			surface.blit(tile, screenpos)

def draw_entitylayer(surface, entitylayer, view, spriteset):
	for entity in entitylayer.entities:
		offsetpos = view.transform((entity.rect[0], entity.rect[1]))
		screenrect = (offsetpos[0], offsetpos[1], entity.rect[2], entity.rect[3])
		surface.fill((0, 255, 0), screenrect)

def draw_player(surface, player, view, spriteset):
	offsetpos = view.transform((player.rect[0], player.rect[1]))
	screenrect = (offsetpos[0], offsetpos[1], player.rect[2], player.rect[3])
	surface.fill((255, 0, 0), screenrect)
