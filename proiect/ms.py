#Minesweeper :D
import random

class Minesweeper:

    def place_scores(self):
        #cautam fiecare mina plasata anterior
        # si ii updatam viecare vecin
        # daca exista overlap (spre exemplu 2 bombe sa aiba acelasi vechin)
        # crestem scorul acelei celule
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j]=="M":
                    #updating vecinii :D

                    #              sus       jos  | st      dr    | jdr   sst   |   jst   sdr
                    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),(1,1),(-1, -1),(1,-1),(-1,1)]

                    for dr, dc in directions:
                        ni, nj = i + dr, j + dc
                                #ni si nj sunt indexi celulei vecine
                                #iar mai jos verificam daca vecinul curent exista (ie suntem pe o celula la margine )
                        if 0 <= ni < len(self.board) and 0 <= nj < len(self.board[ni]):
                            if self.board[ni][nj] != "M":
                                self.board[ni][nj] += 1

    def place_flag(self,x :int ,y :int):

        #debugging stuff
        if not (0 <= x < self.board_size and 0 <= y < self.board_size):
            print("="*10)
            print(f"Coordonate invalide! x:{x} y:{y}")
            print("="*10)
            return
        #still debugging , functia asta trebuie doar sa puna un flag si sa creasca un contor (sau sa scada)
        if self.board[x][y]=='M':
            print("="*10)
            print("Ai prins o bomba!")
            print("="*10)
        self.board[x][y]='F'
        self.flags+=1
        

    def init_mines(self,tabla:list[list],dificultate:str,n:int):
        
        #initializam numarul de bombe bazat pe dificultate
        if dificultate=="easy":
            k_mines=n//2
        elif dificultate=="medium":
            k_mines=int(random.randint(n//4,n//2))
        elif dificultate=="hard":
            k_mines=int(random.randint(n//2,n))
        
        while k_mines:
            x=int(random.randint(0,n-1))
            y=int(random.randint(0,n-1))
            while tabla[x][y]=='M':
                x=int(random.randint(0,n-1))
                y=int(random.randint(0,n-1))
            tabla[x][y]='M'
            print(f"Avem {k_mines} si am pus una la [{x}][{y}]")
            k_mines-=1

            

    def make_board(self,board_size):
        board=[]
        #facem tabla plina cu  'E' pt ca nu are nmk                             
        for i in range(board_size):
            l=[]
            for j in range(board_size):
                l.append(0)
            board.append(l)
        
        return board
    
    def __init__(self, board_size=4, difficulty="medium"):
        self.board_size=int(board_size)
        self.dif=str(difficulty)
        self.flags=0
        
        print(f"initializat tabla cu board size:{self.board_size}, dif: {self.dif}")
        self.board  = self.make_board(board_size)
        self.init_mines(self.board,self.dif,self.board_size)
        self.place_scores()
        #todo maybe calculam scorurile
        #todo place flag
        #todo place mutare

    def __str__(self):
        rez="Matricea afisata\n"
        for linie in self.board:
            for cell in linie:
                rez+=f"{cell} "
            rez+='\n'
        return rez


n=7
game=Minesweeper(n,"medium")
print(game)
print()
for i in range(random.randint(1,7)):
    game.place_flag(random.randint(0,n-1),random.randint(0,n-1))   
print(game)