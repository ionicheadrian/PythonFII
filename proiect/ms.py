#Minesweeper :D
#todo
#do logic for reveal
#gui
#implement gui
#pasii de joc
#winning condition
#scor pe flag 
#scos + adaugat flagurile
#MAKE AI >:)
import random

class Minesweeper:
    class bcolors:
                HEADER = '\033[95m'
                OKBLUE = '\033[94m'
                OKCYAN = '\033[96m'
                OKGREEN = '\033[92m'
                WARNING = '\033[93m'
                FAIL = '\033[91m'
                ENDC = '\033[0m'
                BOLD = '\033[1m'
                UNDERLINE = '\033[4m'

    def reveal(self,x,y):
        if self.show_board[x][y]!=0:
            return
        if self.show_board[x][y] != self.board[x][y]:
            return
        self.show_board[x][y]=self.board[x][y]

        if self.board[x][y] == 0:
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1),(1,1),(-1, -1),(1,-1),(-1,1)]
            for dr,dc in directions:
                if 0<= x + dr < self.board_size and 0 <= y + dc < self.board_size:
                    self.reveal(x+dr,y+dc)





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
        self.show_board[x][y]='F'
        self.flags+=1
        

    def init_mines(self,tabla:list[list],dificultate:str,n:int):
        
        #initializam numarul de bombe bazat pe dificultate
        if dificultate=="easy":
            k_mines=n//2
        elif dificultate=="medium":
            k_mines=int(random.randint(n//4,n//2))
        elif dificultate=="hard":
            k_mines=int(random.randint(n//2,n))
        
        print(f"Avem {k_mines}")

        while k_mines:
            x=int(random.randint(0,n-1))
            y=int(random.randint(0,n-1))
            while tabla[x][y]=='M':
                x=int(random.randint(0,n-1))
                y=int(random.randint(0,n-1))
                print(f"ai la {x} si {y}")
            tabla[x][y]='M'
            print(f"ai la {x} si {y}")
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
        self.show_board = [row[:] for row in self.board] #acum chiar ca am copiat board ul
        self.init_mines(self.board,self.dif,self.board_size)
        self.place_scores()
        #todo place mutare

    def __str__(self):
        
        rez=''
        for i in range(self.board_size):
            for j in range(self.board_size):
                cell=self.show_board[i][j]

                if cell == "M":
                    rez += self.bcolors.OKBLUE + "0" + self.bcolors.ENDC + " "
                if cell == "F":
                    rez += self.bcolors.BOLD + cell + self.bcolors.ENDC +" "
                elif isinstance(cell, int) and True == True:            #todo add logit pt aratat scorurile
                    if cell == 0:
                        rez += self.bcolors.OKBLUE + "0" + self.bcolors.ENDC + " "
                    elif cell == 1:
                        rez += self.bcolors.WARNING + str(cell) + self.bcolors.ENDC + " "
                    elif cell == 2:
                        rez += self.bcolors.OKGREEN + str(cell) + self.bcolors.ENDC + " "
                    else:
                        rez += self.bcolors.HEADER + str(cell) + self.bcolors.ENDC + " "
            rez+="\n"
        return rez




n=7
game=Minesweeper(n,"hard")
# print(game)
# print()
# for i in range(random.randint(1,7)):
#     game.place_flag(random.randint(0,n-1),random.randint(0,n-1))   
# print(game)

print(game)
comanda=input("comanda: ")
while comanda!="exit":
    if comanda == "place_flag":
        x=int(input("     Scrie x:"))
        y=int(input("     Scrie y:"))
        game.place_flag(x,y)
    if comanda == "reveal":
        x=int(input("     Scrie x:"))
        y=int(input("     Scrie y:"))
        game.reveal(x,y)
    print(game)
    comanda=input("comanda: ")
