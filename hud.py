#!/usr/bin/env python

import os, simplejson
import pygame as pg

# Managing the HUD-elements
class Hud:
	def __init__(self, window_resolution, view_rect):
		self.window_resolution = window_resolution
		self.view_rect = view_rect
		self.sprites = {}
		# Elements:
		self.main_frame = Frame()
		self.health_bar = Bar()
		self.mana_bar = Bar()

	# Load spritesheet and configuration files.
	def load_files(self, filepath_sheet, filepath_cfg):
		if os.path.exists(filepath_sheet) and os.path.exists(filepath_cfg):
			sheet = pg.image.load(filepath_sheet).convert()
			sheet.set_colorkey((255, 0, 255))
			try:
				stream = open(filepath_cfg, 'r')
				items = [simplejson.loads(line) for line in stream.readlines()]
				stream.close()
				for item in items:
					self.sprites[item["name"]] = sheet.subsurface(item["x"], item["y"], item["w"], item["h"])
			except:
				print ""
		else:
			print ""

	# Load elements with rect and image or color.
	def load_elements(self):
		if len(self.sprites) > 0:
			self.health_bar.load(self.sprites["bar"], (self.view_rect[2] + self.view_rect[0] * 2, 8))
			self.mana_bar.load(self.sprites["bar"], (self.view_rect[2] + self.view_rect[0] * 2, 33))
			self.main_frame.load(background_color=(18, 18, 18),
							highlight_color=(255, 215, 0),
							background_rects=[(0, 0, 650, 10), (650, 0, 160, 600),
											(0, 490, 650, 110), (0, 10, 10, 480)],
							highlight_rects=[(10, 8, 642, 2), (650, 10, 2, 482),
											 (8, 490, 642, 2), (8, 8, 2, 482)])

	# Load files and elements.
	def load(self, filepath_sheet, filepath_cfg):
		self.load_files(filepath_sheet, filepath_cfg)
		self.load_elements()

	# Draw all elements.
	def draw(self, surface):
		self.main_frame.draw(surface)
		self.health_bar.draw(surface)
		self.mana_bar.draw(surface)
		


# Base for HUD-elements.
class Base(object):
	def __init__(self):
		self.rect = None
		self.image = None
		self.hide = True

	def load(self, image, position):
		self.image = image
		size = image.get_size()
		self.rect = pg.Rect(position[0], position[1], size[0], size[1])



# Background (example: frame around the view window)
class Frame():
	def __init__(self):
		self.background_color = ()
		self.highlight_color = ()
		self.background_rects = []
		self.highlight_rects = []

	def load(self, background_color, highlight_color, background_rects, highlight_rects):
		self.background_color = background_color
		self.highlight_color = highlight_color
		self.background_rects = background_rects
		self.highlight_rects = highlight_rects

	def update(self):
		pass

	def draw(self, surface):
		for rect in self.background_rects:
			pg.draw.rect(surface, self.background_color, rect)
		for rect in self.highlight_rects:
			pg.draw.rect(surface, self.highlight_color, rect)



# Progressbar (example: player's health)
class Bar(Base):
	def __init__(self):
		super(Bar, self).__init__()
		self.percentage = 0
		self.progress_width = 0
		self.progress_color = (255, 0, 0)

	def update(self, value_now, value_max):
		self.progress_width = int((float(self.rect[2]) / value_max) * value_now)

	def draw(self, surface):
		tmp_rect = pg.Rect(self.rect)
		tmp_rect.width = self.progress_width
		pg.draw.rect(surface, self.progress_color, tmp_rect)
		surface.blit(self.image, self.rect)



# Itemslot (example: slots in player's backpack)
class Slot(Base):
	def __init__(self):
		super(Slot_Lefthand, self).__init__()

	def update(self):
		pass

	def draw(self):
		pass

