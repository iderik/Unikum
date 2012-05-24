import os, sys
import pygame
from pygame.locals import *



class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.looping = self.model.looping
        self.clock = pygame.time.Clock()
        self.loop()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                self.model.mouse_position = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                if event.button in (1, 2, 3):   # left, middle or right
                    pass
                elif event.button in (4, 5):    # scroll up or down
                    pass
            elif event.type == MOUSEBUTTONUP:
                if event.button in (1, 2, 3):   # left, middle or right
                    pass
                elif event.button in (4, 5):    # scroll up or down
                    pass
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
            elif event.type == KEYUP:
                pass
    
    # Main game loop
    # QUESTION: Update all and then draw all or keep current method?
    def loop(self):
        while self.model.looping:
            self.model.map.update()
            self.view.map.draw_layer_ground()
            self.model.player.update()
            self.view.player.draw()
            self.model.hud.update()
            self.view.hud.draw()
            self.events()
            pygame.display.update()
            self.clock.tick(self.model.FPS)
