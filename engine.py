import vector
from pygame.locals import *

def clamp(lower, upper, val):
	if val < lower:
		return lower
	elif val > upper:
		return upper
	else:
		return val

def update_world(world, keys, step):
	update_player(world.player, keys, step)

def update_player(player, keys, step):
	# For testing
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

