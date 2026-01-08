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
    
    def show_endframe(self, message_type):
        """
        Afiseaza overlay-ul de final (victorie sau înfrângere)
        Args:
            message_type (str): "win" sau "lose"
        """
        if message_type == "lose":
            self.board.reveal_bombs() 
        self.draw()
        
        #overlay semitransparent frumos asa :D
        overlay = pygame.Surface((LATIME, INALTIME))
        overlay.set_alpha(200)
        overlay.fill((26, 26, 46))
        self.screen.blit(overlay, (0, 0))
        
        #Creem mesajul si culoarea in functie de message_type
        if message_type == "win":
            message = "VICTORY!!"
            color = GREEN
            sub_message = f"Completed in {int(pygame.time.get_ticks() / 1000)}s!"
        else:  # "lose"
            message = "GAME OVER "
            color = RED
            sub_message = "Better luck next time!"           
        
        font_large = pygame.font.Font(None, 72)
        text = font_large.render(message, True, color)
        text_rect = text.get_rect(center=(LATIME // 2, INALTIME // 2 - 50))
        self.screen.blit(text, text_rect)
        
        font_medium = pygame.font.Font(None, 40)
        sub_text = font_medium.render(sub_message, True, (236, 240, 241))
        sub_rect = sub_text.get_rect(center=(LATIME // 2, INALTIME // 2 + 20))
        self.screen.blit(sub_text, sub_rect)
        
        font_small = pygame.font.Font(None, 30)
        restart_text = "Press R to restart or ESC to exit"
        restart = font_small.render(restart_text, True, (149, 165, 166))
        restart_rect = restart.get_rect(center=(LATIME // 2, INALTIME // 2 + 80))
        self.screen.blit(restart, restart_rect)
        
        pygame.display.flip()
        
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    self.running = False
                    return False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        return True
                    elif event.key == pygame.K_ESCAPE: 
                        self.playing = False
                        self.running = False
                        return False
            
            self.clock.tick(FPS)
        
        return False
    
    
    
        
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
                                if self.show_endframe("lose")==True:
                                        self.board=Board(self.dif)
                                        print("Board nou generat!")
                                        
                                        
                                        
                                #NU AVEM VOIE SA DAM REVEAL PESTE FLAG
                            elif celula.flagged == False:
                                if celula.type == 0:#daca avem celula goala
                                    self.board.flood_reveal(row, col)
                                else:
                                    celula.revealed = True
                                
                                print(f"Clicked on cell ({row}, {col}) - Type: {celula.type}")
                                
                                if self.board.check_win():
                                    if self.show_endframe("win") == True:
                                        self.board=Board(self.dif)
                                        print("Board nou generat!")
                                
                    
                    elif event.button == 3:
                        x, y = pygame.mouse.get_pos()
                        row = x // TILESIZE
                        col = y // TILESIZE
                        if 0 <= row < ROWS and 0 <= col < COLS:
                            celula = self.board.board_list[row][col]
                            if not celula.revealed:
                                celula.flagged = not celula.flagged
                                if self.board.check_win():
                                    self.show_endframe("win")
                                    
                                
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