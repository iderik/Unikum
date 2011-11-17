
class Layer:
	pass

class TileLayer(Layer):

	def __init__(self, tiles, tilesize):
		self.tiles = tiles
		self.tilesize = tilesize
		self.size = (len(tiles[0]), len(tiles))

	def is_inside(self, position):
		return position[0] >= 0 and position[0] < self.size[0] and \
				position[1] >= 0 and position[1] < self.size[1]

	def screen_to_layer(self, position):
		return (int(position[0]/self.tilesize[0]), int(position[1]/self.tilesize[1]))

	def layer_to_screen(self, position):
		return (position[0]*self.tilesize[0], position[1]*self.tilesize[1])

	def get_tile(self, position):
		if not self.is_inside(position):
			return None
		return self.tiles[position[1]][position[0]]

class EntityLayer(Layer):
	def __init__(self, size):
		self.size = size
		self.entities = []

	def add_entity(self, entity):
		self.entities.append(entity)
