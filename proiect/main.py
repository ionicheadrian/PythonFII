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
                        x, y = pygame.mouse.get_pos()
                        row = x // TILESIZE
                        col = y // TILESIZE
                        if 0 <= row < ROWS and 0 <= col < COLS:
                            #AM DAT DE BOMBA
                            celula = self.board.board_list[row][col]
                            if celula.type == "x" and celula.flagged == False:
                                print(f"Clicked on cell ({row}, {col}) SI E BOMBA")
                                celula.revealed = True
                                celula.image = c_exploded
                                self.draw()
                                
                                # Afișează text GAME OVER
                                font = pygame.font.Font(None, 74)
                                text = font.render("GAME OVER!", True, RED)
                                text_rect = text.get_rect(center=(LATIME//2, INALTIME//2))
                                self.screen.blit(text, text_rect)
                                
                                pygame.display.flip()
                                pygame.time.wait(2000)
                                
                                # Board nou!
                                self.board = Board(self.dif)
                                print("Board nou generat!")
                                #NU AVEM VOIE SA DAM REVEAL PESTE FLAG
                                
                            elif celula.flagged == False:
                                if celula.type == 0:#daca avem celula goala
                                    self.board.flood_reveal(row, col)
                                else:
                                    celula.revealed = True
                                
                                print(f"Clicked on cell ({row}, {col}) - Type: {celula.type}")
                                
                                if self.board.check_win():
                                    self.draw()
                                    font = pygame.font.Font(None, 74)
                                    text = font.render("AI CÂȘTIGAT!", True, GREEN)
                                    text_rect = text.get_rect(center=(LATIME//2, INALTIME//2))
                                    self.screen.blit(text, text_rect)
                                    
                                    pygame.display.flip()
                                    pygame.time.wait(3000)
                                    self.board = Board(self.dif)
                                    print("Board nou generat!")
                                
                    
                    elif event.button == 3:
                        x, y = pygame.mouse.get_pos()
                        row = x // TILESIZE
                        col = y // TILESIZE
                        if 0 <= row < ROWS and 0 <= col < COLS:
                            celula = self.board.board_list[row][col]
                            if not celula.revealed:
                                celula.flagged = not celula.flagged
                                
                #GAME RESET 
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_r:
                        self.playing=False    
                    if event.key==pygame.K_w:
                        n=range(len(self.board.board_list))
                        for row in n:
                            for col in n:
                                celula= self.board.board_list[row][col]
                                if celula.type == "x":
                                    celula.revealed = not celula.revealed    
                                
                                
                                
            
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
dif=input("dificultatea? : ")
game = Game(dif)
while game.running:
    game.new_game()
    game.run_game()

pygame.quit()