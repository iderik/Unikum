import vector 

class View:
	def __init__(self, size):
		self.offset = (0, 0)
		self.size = size
	
	def center_at(self, center):
		self.offset = vector.sub(center, vector.div(self.size, 2))

	def offset_at(self, offset):
		self.offset = offset

	def transform(self, position):
		return vector.add(position, self.offset)

