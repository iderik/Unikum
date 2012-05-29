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
        self.model.window.blit(self.model.sprites.sprites[1], (10, 10)) # For testing only!



class Map:
    def __init__(self, model):
        self.model = model

    # FIXME: There are still some definitions here which should be in model.
    def draw(self, layer):
        for y in range(11):
            for x in range(15):
                map_position = vector.sub((x, y), self.model.player.position)
                sprite_id = layer[map_position[0]][map_position[1]]
                sprite_image = self.model.sprites.sprites[sprite_id]
                self.model.window.blit(sprite_image, vector.add((x * 32, y * 32), self.model.camera.offset))



class Hud:
    def __init__(self):
        pass
    
    def draw(self):
        pass
