import vector 

# View of enviroment in the world.
# FIXME: Was designed for a 2 length tuple but is now a Pygame.Rect (custom 4 length tuple).
class View:
	def __init__(self, rect):
		self.offset = (0, 0)
		self.rect = rect
	
	def center_at(self, center):
		self.offset = vector.sub(center, vector.div((self.rect[2], self.rect[3]), 2))

	def offset_at(self, offset):
		self.offset = offset

	def transform(self, position):
		return vector.sub(position, self.offset)

