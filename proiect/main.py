import pygame
from setari import *
from componente import *

class Game:
    
    def __init__(self,dif:str):
        pygame.init()
        self.screen = pygame.display.set_mode((LATIME, INALTIME))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.dif = dif
        
    def new_game(self):
        self.playing = True
    
    def run_game(self):
        self.playing = True
        
        while self.playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pass
            # game logic
            self.draw()
            pygame.display.flip()
            self.clock.tick(FPS)
        
        # self.check_win()
        
    def draw(self, board_surface:pygame.surface):
        

        self.screen.fill((200, 200,74))
        # deseneaza board-ul aici

# Main loop
game = Game("easy")
while game.running:
    game.new_game()
    game.run_game()
    
    
pygame.quit()