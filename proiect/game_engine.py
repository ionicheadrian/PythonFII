import pygame
from setari import *
from componente import *

class Game_engine:
    def __init__(self, dif: str):
        self.dif = dif
        self.playing = False
        self.board = None
        
        # TOT CE INSEAMNA TIMERE + WIN / LOSE STATE
        self.first_click = True
        self.start_time = 0
        self.timp = 0
        self.game_over = False
        self.victory = False
        
        # stats
        self.k_mines = 0  # minele in total 
        self.mines = 0  # minele ramase
    
    def new_game(self):
        """FUNCTIE CARE INITIALIZEAZA UN JOC NOU"""
        self.playing = True
        self.board = Board(self.dif)  # Tabla fara mine inca!
        self.first_click = True
        self.timp = 0
        self.game_over = False
        self.victory = False
        
        # Calculam nr de mine bazat pe ce dificultate a ales jucatorul
        n = ROWS
        if self.dif == "easy":
            self.k_mines = int(n * n * 0.15)  # 15% din celule sunt bombe
        elif self.dif == "medium":
            self.k_mines = int(n * n * 0.2)  # 20% 
        elif self.dif == "hard":
            self.k_mines = int(n * n * 0.25)  # 25% 
        
        self.mines = self.k_mines
    
    def update_timer(self):
        """Actualizam timerul (DOAR DACA este un joc activ deci avem nevoie de self.playing)"""
        if self.playing and not self.first_click and not self.game_over:
            self.timp = int(pygame.time.get_ticks() / 1000 - self.start_time)
    
    def handle_click(self, type: int, row, col):
        """Functie care gestioneza click-ul
        
        Args:
            type (int): tipul clickului; 1 - click stanga ; 3 - click dreapta;
            row (int): coordonata pt linie (i)
            col (int): coordonata pt coloana (j)

        Returns:
            str: "continue", "win" sau "lose"
        """
        # cazurile de baza intre starile jocului
        if not self.playing or self.game_over:
            return "continue"
        
        if not (0 <= row < ROWS and 0 <= col < COLS):
            return "continue"
        
        celula = self.board.board_list[row][col]
        
        # PRIMUL CLICK - acum geneream bombele (ca sa nu existe meciuri in care se prierde din prima)
        if self.first_click and type == 1:  # Doar la click stanga
            # print(f"primul click la ({row}, {col})")
            self.board.place_mines(row, col)
            self.first_click = False
            self.start_time = pygame.time.get_ticks() / 1000
            celula = self.board.board_list[row][col]
        
        # Click dreapta poate fi si inainte de primul click stanga
        if self.first_click and type == 3:
            # Permitem flag-uri inainte de primul click, dar nu incepem timer-ul
            if not celula.revealed:
                celula.flagged = not celula.flagged
                if celula.flagged:
                    self.mines -= 1
                else:
                    self.mines += 1
            return "continue"
        
        if type == 1:
            # am apasat pe click stang
            # am dat click pe o bomba \/
            if celula.type == "x" and not celula.flagged:
                celula.revealed = True
                celula.image = c_exploded
                self.board.reveal_bombs()
                self.game_over = True
                return "lose"
            
            # am dat click pe o celul libera
            if not celula.flagged:
                if celula.type == 0:
                    # flood reveal
                    self.board.flood_reveal(row, col)
                else:
                    celula.revealed = True
                
                # mereu verificam winning condition
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
                
                # Verificam daca am castigat
                if self.board.check_win():
                    self.game_over = True
                    self.victory = True
                    return "win"
        return "continue"
   
    def necuratu(self):
        """Dam toggle la toate bombele ca sa putem vedea win / lose condition * those who know*
            mai mult pentru debugging , dar functia da reveal la toate bombele (fara ca jocul sa detecteze win)
        """
        #daca nu am generat minele inca, nu putem face debug
        if not self.board.mines_generated:
            return
            
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