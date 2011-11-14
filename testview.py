from view import View
import unittest

class TestView(unittest.TestCase):

	def setUp(self):
		pass

	def test_identity_transform(self):
		view = View((5, 7))
		self.assertEqual(view.transform((3, 4)), (3, 4))
		pass

	def test_transform_offset(self):
		view = View((5, 7))
		view.offset_at((2, 1))
		self.assertEqual(view.transform((3, 2)), (5, 3))

	def test_transform_center(self):
		view = View((5.0, 7.0))
		view.center_at((2.0, 1.0))
		self.assertEqual(view.transform((3.0, 2.0)), (2.5, -0.5))
                                                          

if __name__ == '__main__':
	unittest.main()
