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
        if self.flagged and not self.revealed:
            board_surface.blit(c_flag, (self.x, self.y))
        elif self.revealed:
            board_surface.blit(self.image, (self.x, self.y))  # Fix aici!
        else:
            board_surface.blit(c, (self.x, self.y))
            
                 
    def __repr__(self):
        return self.type


class Board:
    def __init__(self,dif:str):
        self.board_surface=pygame.Surface((LATIME,INALTIME))
        self.board_list=[]
        for l in range(ROWS):
            a=[]
            for col in range(COLS):
                a.append(Cell(l,col,c,0))
            self.board_list.append(a)
        self.place_mines(dif)
        self.place_scores()
        
        
    def place_mines(self, dif:str):
            k_mines=0
            n=ROWS
            if dif == "easy":
                k_mines= int(n*n*0.15)
            elif dif =="medium":
                k_mines= int(n*n*0.2)
            elif dif == "hard":
                k_mines = int(n*n*0.25)
            print(f"avem {k_mines} mine")
            while k_mines:
                x=int(random.randint(0,n-1))
                y=int(random.randint(0,n-1))
                
                if self.board_list[x][y].type == 0:
                    self.board_list[x][y].image =c_mina
                    self.board_list[x][y].type = "x"
                    # print(f"avem asta la {x} si {y} : {self.board_list[x][y].type}")
                    k_mines-=1
                
                
                
        
    def place_scores(self):
        for i in range(len(self.board_list)):
            for j in range(len(self.board_list[i])):
                if self.board_list[i][j].type == "x":  # daca este mina
                    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
                    for dr, dc in directions:
                        ni, nj = i + dr, j + dc
                        # verif daca vecinul exista
                        if 0 <= ni < len(self.board_list) and 0 <= nj < len(self.board_list[ni]):
                            #daca vecinu NU este mina atunci incrementam
                            if self.board_list[ni][nj].type != "x":
                                self.board_list[ni][nj].type += 1
        
    #dupa ce am calculat scorurile corect, asignam si imaginile 
        for i in range(len(self.board_list)):
            for j in range(len(self.board_list[i])):
                cell_type=self.board_list[i][j].type
                if cell_type == 0:
                    self.board_list[i][j].image=c_goala
                elif cell_type != "x" and cell_type>0:
                    #inseamna ca suntem pe o celula care are scor (1-8)
                    self.board_list[i][j].image=numere[cell_type-1] # DUPA  3 ORE MI AM DAT SEAMA NUMERE ESTE 1-8 SI EU CAUTAM 0-7..... ;(
        
    def flood_reveal(self,row,col):
        #cazurile de baza
        if row < 0 or row >= len(self.board_list):
            return
        if col < 0 or col >= len(self.board_list[0]):
            return
        celula = self.board_list[row][col]
        
        if celula.revealed or celula.flagged:
            return
        if celula.type == "x":
            return
        celula.revealed=True
        if celula.type != 0:
            return
        
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),(1,1),(-1, -1),(1,-1),(-1,1)]
        
        for dr,dc in directions:
            self.flood_reveal(row + dr, col + dc)
    
    def reveal_bombs(self):
        for row in self.board_list:
            for celula in row:
                if celula.type=="x":
                    celula.revealed = True
    
    def check_win(self):    
        for row in self.board_list:
            for celula in row:
                if celula.revealed == False:
                    if celula.type == "x":
                        if celula.flagged == False:
                            return False
        return True
    
        
    def draw(self):
        for row in self.board_list:
            for cell in row:
                cell.draw(self.board_surface)