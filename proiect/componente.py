import pygame
from setari import *




class Cell:
    def __init__(self,x,y,image,type,revealed=False,flagged=False):
        self.x=x*TILESIZE
        self.y=y*TILESIZE
        self.image=image
        self.revealed=revealed
        self.flagged=flagged
        self.type=type
        
    def draw (self, board_surface:pygame.Surface):
        """Functie care deseneaza corect celula dupa caracteristicile ei : flagged, revealed, empty, cu 74 de vecini
        Args:
            board_surface (pygame.Surface): suprafata pe care desenam tabla
        """
        if self.flagged==False and self.revealed==True:
            board_surface.blit(self.image(self.x,self.y))
        elif self.flagged==True and self.revealed==False:
            board_surface.blit(c_flag,(self.x,self.y))
        elif self.revealed==False:
            board_surface.blit(c,(self.x,self.y))
            
                 
    def __repr__(self):
        return self.type


class Board:
    def __init__(self):
        self.board_surface=pygame.Surface(LATIME,INALTIME)
        self.board_list=[]
        for l in range(ROWS):
            a=[]
            for col in range(COLS):
                a.append(Cell(l,col,c,'.'))
            self.board_list.append(a)
        self.place_mines()
        self.place_scores()
        
        
        def place_mines(self):
            pass
        
        def place_scores(self):
            pass
        