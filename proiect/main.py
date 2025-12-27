import pygame
from setari import *
from componente import *

class Game:
    
    def __init__(self):
        pygame.init()  # important!
        self.screen = pygame.display.set_mode((LATIME, INALTIME))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        
    def new_game(self):
        
        self.playing = True
    
    def run_game(self):
        self.playing = True
        
        while self.playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    self.running = False
            
            # game logic
            self.draw()
            pygame.display.flip()
            self.clock.tick(FPS)
        
        # self.check_win()
        
    def draw(self):

        self.screen.fill((200, 200,74))
        # desenează board-ul aici

# Main loop
game = Game()
while game.running:
    game.new_game()
    game.run_game()
    
    
pygame.quit()