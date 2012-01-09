#!/usr/bin/env python

import vector
import unittest

class TestVector(unittest.TestCase):

	def test_x(self):
		self.assertEqual(vector.get_x((3, 4)), 3)
		self.assertEqual(vector.get_x((3.1, 4.2)), 3.1)
	def test_y(self):
		self.assertEqual(vector.get_y((3, 4)), 4)
		self.assertEqual(vector.get_y((3.1, 4.2)), 4.2)
	def test_add(self):
		self.assertEqual(vector.add((1, 2), (3, 4)), (4, 6))
		self.assertEqual(vector.add((1.5, 2.5), (3.1, 4.2)), (4.6, 6.7))
	def test_sub(self):
		self.assertEqual(vector.sub((1, 2), (3, 1)), (-2, 1))
		self.assertEqual(vector.sub((1.5, 2.5), (3.1, 1.2)), (-1.6, 1.3))
	def test_mul(self):
		self.assertEquals(vector.mul((3, 4), 2), (6, 8))
		self.assertEquals(vector.mul((3.1, 4.2), 2.0), (6.2, 8.4))
	def test_div(self):
		self.assertEquals(vector.div((3, 4), 2), (1, 2))
		self.assertEquals(vector.div((3.1, 4.2), 2.0), (1.55, 2.1))
	def test_neg(self):
		self.assertEquals(vector.neg((3, 4)), (-3, -4))
		self.assertEquals(vector.neg((3.1, 4.2)), (-3.1, -4.2))

if __name__ == '__main__':
	unittest.main()
