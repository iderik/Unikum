from view import View
import vector

import pygame
from pygame.locals import *

def draw_world(surface, world, view, tilesets):
	draw_tilelayer(surface, world.tilelayer, view, tilesets[1])
	draw_tilelayer(surface, world.transitionlayer, view, tilesets[1])
	draw_entitylayer(surface, world.entitylayer, view, tilesets[0])
	draw_player(surface, world.player, view, tilesets[0])

def draw_tilelayer(surface, tilelayer, view, tileset):
	for y in range(tilelayer.size[1]):
		for x in range(tilelayer.size[0]):
			screenpos = view.transform((tilelayer.tilesize[0]*x, tilelayer.tilesize[1]*y))
			surface.blit(tileset[tilelayer.get_tile((x, y))], screenpos)

def draw_entitylayer(surface, entitylayer, view, spriteset):
	for entity in entitylayer.entities:
		draw_entity(surface, entity, view, spriteset)

def draw_entity(surface, entity, view, spriteset):
	offsetpos = view.transform(vector.sub(entity.position, vector.div(entity.size, 2)))
	surface.blit(spriteset[entity.sprite_id], offsetpos)

def draw_player(surface, player, view, spriteset):
	draw_entity(surface, player, view, spriteset)
