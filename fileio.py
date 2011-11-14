#!/usr/bin/env python

import sys, os, simplejson

class Stream:
	def __init__(self):
		self.parser = Parser()

	def stream_open(self, filepath, operator, position):
		if os.path.exists(filepath):
			stream = open(filepath, operator)
			if position is not 0:
				if end_position(filepath) > 0:
					stream.seek(position)
			return stream
		else:
			print "[ERR] Couldn't open fileobject, filepath doesn't exists."
			print "[+++] Filepath=%s" % filepath
			return None

	def read(self, filepath, operator='r', position=0):
		data = []
		stream = stream_open(filepath, operator, position)
		if stream is not None:
			data = stream.readlines()
			stream.close()
		return data

	def write(self, filepath, data, operator='w', position=0):
		stream = stream_open(filepath, operator, position)
		if stream is not None:
			stream.write(data)
			stream.close()

	def end_position(self, filepath):
		stream = stream_open(filepath, 'r', 0)
		if stream is not None:
			stream.seek(0, os.SEEK_END)
			position = stream.tell()
			stream.close()
			return position
		else:
			return None

	def search_position(self, filepath, search_string):
		positions = []
		stream = stream_open(filepath, 'r', 0)
		if stream is not None:
			for line in stream.readlines():
				if search_string in line:
					positions.append(stream.tell())
		return positions
					

class Parser:
	def __init__(self):
		pass

	def JSON_decode(self, data):
		elements = {}
		try:
			elements = simplejson.loads(data)
		except:
			print "[ERR] Couldn't parse JSON"
			print "[+++] Data=%s" % data

	def JSON_encode(self, data):
		pass
