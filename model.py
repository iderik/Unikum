import os, sys, simplejson
import pygame
from pygame.locals import *



class Model:
    def __init__(self):
        self.player = Player('Sture')
        self.map = Map()
        self.hud = Hud()
        self.sprites = Sprites((32, 32))
        self.camera = Camera((100, 100, 15 * self.sprites.size[0], 11 * self.sprites.size[1]))
        self.looping = True
        self.FPS = 30
        self.mouse_position = (0, 0)
        self.window_caption = 'Unikum game (0.1 ALPHA)'
        self.window_resolution = (640, 480)
        self.window = pygame.display.set_mode(self.window_resolution)
        pygame.init()
        self.load()
        
    def load(self):
        self.player.load('data/players')
        self.map.load('data/map/')
        self.hud.load('data/hud.png')
        self.sprites.load('data/media/sprites.png')



class Player:
    def __init__(self, name):
        self.name = name
        self.outfit = None
        self.position = (None, None)
        self.direction = None          # 1 = North, 2 = East, 3 = South, 4 = West
        self.velocity = None
        self.velocity_max = None
        self.health = None
        self.health_max = None
        
    def load(self, filepath):
        try:
            if os.path.exists(filepath):
                stream = open(filepath, 'r')
                lines = [simplejson.loads(line) for line in stream.readlines()]
                stream.close()
                for line in lines:
                    if line['name'] == self.name:
                        for key, value in line.iteritems():
                            vars(self)[key] = value
            else:
                print 'ERROR player.load: Name (%s) doesn\'t exist in %s' % (self.name, filepath)
        except:
            pass
        
    def update(self):
        pass



class Map:
    def __init__(self):
        self.size = None
        self.layer_ground = None
        self.layer_transition = None
        self.layer_object = None
        self.layer_overlay = None
    
    def load(self, dirpath):
        if os.path.exists(dirpath):
            for filename in os.listdir(dirpath):
                stream = open(dirpath + '/' + filename, 'r')
                vars(self)[filename] = [map(int, line.split(',')) for line in stream.readlines()]
                stream.close()
                if filename == 'layer_ground':
                    self.layer_transition = self.layer_transition_generate(self.layer_ground)
        else:
            print 'ERROR map.load: Dirpath (%s) doesn\'t exist.' % dirpath
        if self.layer_ground:
            self.size = (len(self.layer_ground), len(self.layer_ground[0]))

    def update(self):
        pass
    
    def layer_transition_generate(self, layer):
        return None



class Hud:
    def __init__(self):
        self.sheet = None
    
    def load(self, filepath):
        pass
    
    def update(self):
        pass



class Sprites:
    def __init__(self, size):
        self.sprites = []
        self.size = size    # Size of a sprite
        
    def load(self, filepath):
        if os.path.exists(filepath):
            sheet = pygame.image.load(filepath).convert_alpha()
            sheet_size = sheet.get_size()
            for y in range(sheet_size[1] / self.size[1]):
                for x in range(sheet_size[0] / self.size[0]):
                    rectangle = (x * self.size[0], y * self.size[1],
                                 self.size[0], self.size[1])
                    self.sprites.append(sheet.subsurface(rectangle))
        else:
            print 'ERROR sprites.load: File (%s) doesn\'t exist.' % filepath
        
        



class Camera:
    def __init__(self, rectangle):
        self.rectangle = rectangle
        
    def move(self):
        pass