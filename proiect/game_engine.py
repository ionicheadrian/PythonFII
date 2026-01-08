import pygame
from setari import *
from componente import *


class Game_engine:
    def __init__(self, dif: str):
        pygame.init()
        self.screen = pygame.display.set_mode((LATIME, INALTIME))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        
        self.dif = dif
        self.playing = False
        self.board = None
        
        # Timer 
        self.first_click = True
        self.start_time = 0
        self.elapsed_time = 0
        self.game_over = False
        self.victory = False
        
        # Stats
        self.total_mines = 0
        self.mines_left = 0
    
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
    
    def handle_click(self,type:int,row:int,col:int):
        """_summary_

        Args:
            type (int): _description_
            row (int): _description_
            col (int): _description_
        """
        if type == 1: #left click
            print('s a apasat butonu sting')
            if not self.playing or self.game_over:
                return "continue"
        
            if not (0 <= row < ROWS and 0 <= col < COLS):
                return "continue"
            
            celula = self.board.board_list[row][col]
            
            # Primul click pornește timer-ul
            if self.first_click:
                self.first_click = False
                self.start_time = pygame.time.get_ticks() / 1000
            
            # Click pe bombă
            if celula.type == "x" and not celula.flagged:
                celula.revealed = True
                celula.image = c_exploded
                self.board.reveal_bombs()
                self.game_over = True
                return "lose"
            
            # Click pe celulă normală (nu flagged)
            if not celula.flagged:
                if celula.type == 0:  # Celulă goală
                    self.board.flood_reveal(row, col)
                else:
                    celula.revealed = True
                
                # Verifică dacă am câștigat
                if self.board.check_win():
                    self.game_over = True
                    self.victory = True
                    return "win"
            
            return "continue"
    
        elif type == 3: #right clickkk
            print("s a apasat butonu drept")
            if not self.playing or self.game_over:
                return "continue"
            
            if not (0 <= row < ROWS and 0 <= col < COLS):
                return "continue"
            
            celula = self.board.board_list[row][col]
            
            if not celula.revealed:
                celula.flagged = not celula.flagged
                
                # Update mines_left counter
                if celula.flagged:
                    self.mines_left -= 1
                else:
                    self.mines_left += 1
                
                # Verifică dacă am câștigat
                if self.board.check_win():
                    self.game_over = True
                    self.victory = True
                    return "win"
            
            return "continue"
        
    def draw(self):
        self.screen.fill((200, 200, 74))
        # Desenăm tabla
        self.board.draw()
        # Punem board_surface pe screen
        self.screen.blit(self.board.board_surface, (0, 0))

    def update_timer(self):
        """Actualizează timer-ul (doar dacă jocul e activ)"""
        if self.playing and not self.first_click and not self.game_over:
            self.elapsed_time = int(pygame.time.get_ticks() / 1000 - self.start_time)
            
    def get_cellpos(self, x, y):
        """
        Returnează coordonatele celulei la poziția mouse-ului
        Returns:
            tuple: (row, col) sau None
        """
        row = x // TILESIZE
        col = y // TILESIZE
        if 0 <= row < ROWS and 0 <= col < COLS:
            return (row, col)
        return None      
            
            
            
            
