# main.py - modificări complete

import pygame
from setari import *
from componente import *

class Game:
    def __init__(self, dif: str):
        pygame.init()
        self.screen = pygame.display.set_mode((LATIME, INALTIME))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.dif = dif
        
    def new_game(self):
        self.playing = True
        #initializam o tabla (random)
        #tho to do trebuie sa generam tabla dupa primul click :P
        self.board = Board(self.dif)
    
    def run_game(self):
        self.playing = True
        
        while self.playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: 
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        #verificam celula apasata 
                        row = mouse_x // TILESIZE
                        col = mouse_y // TILESIZE
                        if 0 <= row < ROWS and 0 <= col < COLS:
                            self.board.board_list[row][col].revealed = True
                            print(f"Clicked on cell ({row}, {col}) - Type: {self.board.board_list[row][col].type}")
                    
                    elif event.button == 3:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        row = mouse_x // TILESIZE
                        col = mouse_y // TILESIZE
                        if 0 <= row < ROWS and 0 <= col < COLS:
                            cell = self.board.board_list[row][col]
                            if not cell.revealed:
                                cell.flagged = not cell.flagged
            
            self.draw()
            pygame.display.flip()
            self.clock.tick(FPS)
    
    def draw(self):
        self.screen.fill((200, 200, 74))
        # Desenăm tabla
        self.board.draw()
        # Punem board_surface pe screen
        self.screen.blit(self.board.board_surface, (0, 0))


# Main loop
game = Game("easy")
while game.running:
    game.new_game()
    game.run_game()

pygame.quit()