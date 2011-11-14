from view import View
from pygame.locals import *

def render_tilelayer(surface, tilelayer, view, testsprite):
	start = tilelayer.screen_to_layer(view.transform((0, 0)))
	end = tilelayer.screen_to_layer(view.transform(view.size))
	x = 0
	y = 0
	for ty in range(start[1], end[1]+2):
		for tx in range(start[0], end[0]+2):
			if (tx+ty) % 2 == 0:
				surface.blit(testsprite, (x-view.offset[0]%32, y-view.offset[1]%32))
			x += tilelayer.size[0]
		x = 0
		y += tilelayer.size[1]

def render_entitylayer(entitylayer, view):
	pass
