import pygame
from setari import *
from componente import *

class Game_engine:
    def __init__(self, dif: str):
        self.dif = dif
        self.playing = False
        self.board = None
        
        #TOT CE INSEAMNA TIMERE + WIN / LOSE STATE
        self.first_click = True
        self.start_time = 0
        self.elapsed_time = 0
        self.game_over = False
        self.victory = False
        
        #statss
        self.k_mines = 0 #minele in total 
        self.mines = 0 #minele ramase
    
    def new_game(self):
        """FUNCTIE CARE INITIALIZEAZA UN JOC NOU"""
        self.playing = True
        self.board = Board(self.dif)
        self.first_click = True
        self.elapsed_time = 0
        self.game_over = False
        self.victory = False
        
        # acum calculam nr de mine bazat pe ce dificultate a ales jucatorul
        n = ROWS
        if self.dif == "easy":
            self.k_mines = int(n*n*0.15) # 15% din celule sunt bombe
        elif self.dif == "medium":
            self.k_mines = int(n*n*0.2) # 20% 
        elif self.dif == "hard":
            self.k_mines = int(n*n*0.25) # 25% 
        
        self.mines = self.k_mines
    
    def update_timer(self):
        """Actualizam timerul (DOAR DACA este un joc activ deci avem nevoie de self.playing)"""
        if self.playing and not self.first_click and not self.game_over:
            self.elapsed_time = int(pygame.time.get_ticks() / 1000 - self.start_time)
    
    def handle_click(self,type:int,row, col):
        """Functie care gestioneza click-ul
        

        Args:
            type (int): tipul clickului; 1 - click stanga ; 3 - click dreapta;
            row (int): coordonata pt linie (i)
            col (int): coordonata pt coloana (j)

        Returns:
            str: "continue", "win" sau "lose"
        """
        #cazurile de baza intre starile jocului
        if not self.playing or self.game_over:
            return "continue"
        
        if not (0 <= row < ROWS and 0 <= col < COLS):
            return "continue"
        
        celula = self.board.board_list[row][col]
        
        # Mereu primul click stanga / dreapta incepe timer-ul
        if self.first_click:
            self.first_click = False
            self.start_time = pygame.time.get_ticks() / 1000
        
        
        if type == 1:
            #am apasat pe click stang
            #am dat click pe o bomba \/
            if celula.type == "x" and not celula.flagged:
                celula.revealed = True
                celula.image = c_exploded
                self.board.reveal_bombs()
                self.game_over = True
                return "lose"
            
            # am dat click pe o celul libera
            if not celula.flagged:
                if celula.type == 0:
                    #flood reveal
                    self.board.flood_reveal(row, col)
                else:
                    celula.revealed = True
                
                #mereu verificam winning condition
                if self.board.check_win():
                    self.game_over = True
                    self.victory = True
                    return "win"
        elif type == 3:
            if not celula.revealed:
                celula.flagged = not celula.flagged
                
                # Update mines counter
                if celula.flagged:
                    self.mines -= 1
                else:
                    self.mines += 1
                
                # Verifică dacă am câștigat
                if self.board.check_win():
                    self.game_over = True
                    self.victory = True
                    return "win"
        return "continue"
   
    def necuratu(self):
        """Dam toggle la toate bombele ca sa putem vedea win / lose condition * those who know*
            mai mult pentru debugging , dar functia da reveal la toate bombele (fara ca jocul sa detecteze win)
        """
        for row in self.board.board_list:
            for celula in row:
                if celula.type == "x":
                    celula.revealed = not celula.revealed
    
    def get_cellpos(self, x, y):
        """
        Returneaza coordonatele celulei la pozitia mouse ului
        Returns:
            tuple: (row, col) sau None
        """
        row = x // TILESIZE
        col = y // TILESIZE
        if 0 <= row < ROWS and 0 <= col < COLS:
            return (row, col)
        return None
