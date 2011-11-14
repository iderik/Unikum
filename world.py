#!/usr/bin/env python

import sys, os
from numpy import *

class Manager:
	def __init__(self):
		self.layers = []

	def load(self, filepaths):
		for filepath in filepaths:
			if os.path.exists(filepath):
				stream = open(filepath, 'r')
				layer = [map(int, line.split(',')) for line in stream.readlines()]
				stream.close()
				self.layers.append(array(layer))
