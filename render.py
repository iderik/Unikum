import vector
import pygame
from view import View
from pygame.locals import *

# World
def draw_world(surface, world, view, tilesets):
	draw_tilelayer(surface, world.tilelayer, view, tilesets[1])
	draw_tilelayer(surface, world.transitionlayer, view, tilesets[1])
	draw_entitylayer(surface, world.entitylayer, view, tilesets[0])
	draw_player(surface, world.player, view, tilesets[0])

# Tilelayer
def draw_tilelayer(surface, tilelayer, view, tileset):
	for y in range(tilelayer.size[1]):
		for x in range(tilelayer.size[0]):
			screenpos = view.transform((tilelayer.tilesize[0]*x, tilelayer.tilesize[1]*y))
			surface.blit(tileset[tilelayer.get_tile((x, y))], screenpos)

# Entitylayer
def draw_entitylayer(surface, entitylayer, view, spriteset):
	for entity in entitylayer.entities:
		draw_entity(surface, entity, view, spriteset)

# Entity
def draw_entity(surface, entity, view, spriteset):
	offsetpos = view.transform(vector.sub(entity.position, vector.div(entity.size, 2)))
	surface.blit(spriteset[entity.sprite_id], offsetpos)

# Player
def draw_player(surface, player, view, spriteset):
	draw_entity(surface, player, view, spriteset)

# HUD
def draw_hud(surface, hud):
	hud.draw(surface)
