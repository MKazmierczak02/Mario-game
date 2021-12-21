import pygame, sys
from settings import *
from overworld import Overworld
pygame.init()

class Game():
    def __init__(self):
        self.max_level = 3
        self.overworld = Overworld(1,self.max_level,screen)
    
    def run(self):
        self.overworld.run()
        


screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
game=Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()
    
    screen.fill('black')
    game.run()
    pygame.display.update()
    clock.tick(60)