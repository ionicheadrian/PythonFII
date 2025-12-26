import pygame
from setari import *
from componente import *



class Game:
    
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        
    def new_game(self):
        pass
    
    def run_game(self):
        self.playing =True
        
        while self.playing == True:
            self.clock.tick(FPS)
            #game logic
        
        self.check_win()
        
    def draw(self):
        pass
    
    
game= Game()
while True:
    game.new_game()
    game.run_game