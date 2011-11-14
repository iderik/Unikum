
class Layer:
	pass

class TileLayer(Layer):

	def __init__(self, tiles, size):
		self.tiles = tiles
		self.size = size

	def is_inside(self, position):
		return True

	def screen_to_layer(self, position):
		return (int(position[0]/self.size[0]), int(position[1]/self.size[1]))

	def layer_to_screen(self, position):
		return (position[0]*self.size[0], position[1]*self.size[1])

	def get_tile(self, position):
		if not self.is_inside(position):
			return None
		return self.tiles[position[1]][position[0]]

class EntityLayer(Layer):
	pass

