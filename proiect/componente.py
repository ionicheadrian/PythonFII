import random
import pygame
from setari import *

class Cell:
    
    def __init__(self,x,y,image,type,revealed=False,flagged=False):
        # types list
        # "0" -> nu stim ce e (acoperita)
        # "x" -> mina
        # "c" -> cifra (1,2,..8)
        # "/" -> celula goala (nu are vecini bomba si este revealed)
        self.x=x*TILESIZE
        self.y=y*TILESIZE
        self.image=image
        self.revealed=revealed
        self.flagged=flagged
        self.type=type
        
    def draw(self, board_surface: pygame.Surface):
        # FIX: revealed are prioritate - la game over aratam bombele chiar daca sunt flagged
        if self.revealed:
            board_surface.blit(self.image, (self.x, self.y))
        elif self.flagged:
            board_surface.blit(c_flag, (self.x, self.y))
        else:
            board_surface.blit(c, (self.x, self.y))
            
                 
    def __repr__(self):
        return self.type


class Board:
    def __init__(self, dif: str):
        self.board_surface = pygame.Surface((LATIME, INALTIME))
        self.board_list = []
        self.dif = dif
        self.mines_generated = False  # Flag pentru a ști dacă am generat minele
        
        # Creez tabla cu celule goale
        for l in range(ROWS):
            a = []
            for col in range(COLS):
                a.append(Cell(l, col, c, 0))
            self.board_list.append(a)
        
        # NU generam minele aici - se vor genera la primul click!
        
    def place_mines(self, p_linie: int, p_coloana: int):
        """
        Genereaza minele DUPA primul click, asigurandu-se ca prima celula
        SI vecinii ei NU sunt mine (pentru o experienta mai buna)
        
        Args:
            p_linie: randul primului click
            p_coloana: coloana primului click
        """
        if self.mines_generated:
            return  
        
        # calculam nr demine
        k_mines = 0
        n = ROWS
        if self.dif == "easy":
            k_mines = int(n*n*0.15)
        elif self.dif == "medium":
            k_mines = int(n*n*0.2)
        elif self.dif == "hard":
            k_mines = int(n*n*0.25)
        
        
        #AM CREEAT O ZONA INTERZISA
        zonax = set()
        zonax.add((p_linie, p_coloana))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dr, dc in directions:
            ni, nj = p_linie + dr, p_coloana + dc
            if 0 <= ni < ROWS and 0 <= nj < COLS:
                zonax.add((ni, nj))
        
        # Plasam minele, evitand celulele interzise
        mines_placed = 0
        while mines_placed < k_mines:
            x = random.randint(0, n - 1)
            y = random.randint(0, n - 1)
            
            # Verificam daca celula este libera si NU e in zona interzisa
            if self.board_list[x][y].type == 0 and (x, y) not in zonax:
                self.board_list[x][y].image = c_mina
                self.board_list[x][y].type = "x"
                mines_placed += 1
        
        self.place_scores()
        
        self.mines_generated = True
        # print(f"Mine generate cu succes! Prima celula ({p_linie}, {p_coloana}) este sigura.")
        
    def place_scores(self):
        """Calculeaza cati vecini mine are fiecare celula"""
        for i in range(len(self.board_list)):
            for j in range(len(self.board_list[i])):
                if self.board_list[i][j].type == "x":  # daca este mina
                    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
                    for dr, dc in directions:
                        ni, nj = i + dr, j + dc
                        # verif daca vecinul exista
                        if 0 <= ni < len(self.board_list) and 0 <= nj < len(self.board_list[ni]):
                            # daca vecinu NU este mina atunci incrementam
                            if self.board_list[ni][nj].type != "x":
                                self.board_list[ni][nj].type += 1
        
        # dupa ce am calculat scorurile corect, asignam si imaginile 
        for i in range(len(self.board_list)):
            for j in range(len(self.board_list[i])):
                cell_type = self.board_list[i][j].type
                if cell_type == 0:
                    self.board_list[i][j].image = c_goala
                elif cell_type != "x" and cell_type > 0:
                    # inseamna ca suntem pe o celula care are scor (1-8)
                    self.board_list[i][j].image = numere[cell_type - 1]
        
    def flood_reveal(self, row, col):
        """Reveal recursiv pentru celulele goale"""
        # cazurile de baza
        if row < 0 or row >= len(self.board_list):
            return
        if col < 0 or col >= len(self.board_list[0]):
            return
        celula = self.board_list[row][col]
        
        if celula.revealed or celula.flagged:
            return
        if celula.type == "x":
            return
        celula.revealed = True
        if celula.type != 0:
            return
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        
        for dr, dc in directions:
            self.flood_reveal(row + dr, col + dc)
    
    def reveal_bombs(self):
        """Reveal la toate bombele (la game over)"""
        for row in self.board_list:
            for celula in row:
                if celula.type == "x":
                    celula.revealed = True
    
    def check_win(self):
        """Verificam daca jucatorul a castigat"""
        flagged = True
        celulele_revealed = True
        
        for row in self.board_list:
            for celula in row:
                if celula.type == "x":
                    if not celula.flagged:
                        flagged = False
                else:
                    if not celula.revealed:
                        celulele_revealed = False
    
        return flagged or celulele_revealed
    
    def draw(self):
        """Deseneaza tabla"""
        for row in self.board_list:
            for cell in row:
                cell.draw(self.board_surface)