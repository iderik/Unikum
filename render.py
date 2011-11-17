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
		draw_entity(surface, entity, view, spriteset)

def draw_entity(surface, entity, view, spriteset):
	offsetpos = view.transform(vector.sub(entity.position, vector.div(entity.size, 2)))
	screenrect = (offsetpos[0], offsetpos[1], entity.size[0], entity.size[1])
	surface.fill((255, 0, 0), screenrect)

def draw_player(surface, player, view, spriteset):
	draw_entity(surface, player, view, spriteset)
