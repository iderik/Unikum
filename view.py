import os, sys, vector
import pygame
from pygame.locals import *



class View:
    def __init__(self, model):
        self.model = model
        self.player = Player(self.model)
        self.map = Map(self.model)
        self.hud = Hud()
        pygame.display.set_caption(self.model.window_caption)



class Player:
    def __init__(self, model):
        self.model = model
    
    def draw(self):
        self.model.window.blit(self.model.sprites.sprites[1], (10, 10))



class Map:
    def __init__(self, model):
        self.model = model

    # FIXME: Using wrong arguments on vector.sub! 
    def draw_layer_ground(self):
        for y in range(self.model.map.size[1]):
            for x in range(self.model.map.size[0]):
                position = vector.sub((x * self.model.sprites.size[0],
                                       y * self.model.sprites.size[1]),
                                      (self.model.camera.rectangle[0],
                                       self.model.camera.rectangle[1]))
                sprite_id = self.model.map.layer_ground[x][y]
                sprite_surface = self.model.sprites.sprites[sprite_id]
                self.model.window.blit(sprite_surface, position)
                                 
                                 

    def draw_layer_transition(self):
        pass
    
    # At this moment you can only have 1 item on the ground.
    def draw_layer_object(self):
        pass
    
    def draw_layer_overlay(self):
        pass

class Hud:
    def __init__(self):
        pass
    
    def draw(self):
        pass
