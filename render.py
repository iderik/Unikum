from view import View
import vector

import pygame
from pygame.locals import *

def draw_world(surface, world, view, tileset):
	for layer in world.layers:
		draw_tilelayer(surface, layer, view, tileset)

def draw_tilelayer(surface, tilelayer, view, tileset):
	start = tilelayer.screen_to_layer(view.transform((0, 0)))
	end = tilelayer.screen_to_layer(view.transform(view.size))
	x = 0
	y = 0
	alignment = (view.offset[0] % tilelayer.tilesize[0], view.offset[1] % tilelayer.tilesize[1])
	for ty in xrange(start[1], end[1]+2):
		for tx in xrange(start[0], end[0]+2):
			tilepos = (tx, ty)
			if tilelayer.is_inside(tilepos):
				screenpos = vector.sub((x, y), alignment)
				# Scale up the tile 16x16 to 32x32 until we get full size tiles
				tile = pygame.transform.rotozoom(tileset[tilelayer.get_tile((tx, ty))], 0.0, 2.0)
				surface.blit(tile, screenpos)
			x += tilelayer.tilesize[0]
		x = 0
		y += tilelayer.tilesize[1]

def draw_entitylayer(surface, entitylayer, view, tileset):
	pass
