import vector
from pygame.locals import *

# Clamping
def clamp(lower, upper, val):
	if val < lower:
		return lower
	elif val > upper:
		return upper
	else:
		return val

# World
def update_world(world, keys, step):
	update_player(world.player, keys, step)

# Player
def update_player(player, keys, step):
	# FIXME: For testing
	acc = player.acceleration
	if K_a in keys:
		player.velocity = vector.add(player.velocity, (-acc, 0))
	if K_d in keys:
		player.velocity = vector.add(player.velocity, (acc, 0))
	if K_w in keys:
		player.velocity = vector.add(player.velocity, (0, -acc))
	if K_s in keys:
		player.velocity = vector.add(player.velocity, (0, acc))

	player.velocity = (clamp(-player.maxvelocity, player.maxvelocity, player.velocity[0]), \
			clamp(-player.maxvelocity, player.maxvelocity, player.velocity[1]))

	player.position = (player.position[0] + player.velocity[0]*step, \
			player.position[1] + player.velocity[1]*step)

	player.velocity = vector.mul(player.velocity, player.slowdown)

# HUD
def update_hud(hud, world):
	player = world.player
	hud.health_bar.update(player.health, player.health_max)
	hud.mana_bar.update(player.mana, player.mana_max)
