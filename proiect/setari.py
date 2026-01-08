
import pygame
import os



# COLORS (r, g, b)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
DARKGREEN = (0, 200, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BGCOLOUR = DARKGREY


#setarile jocului
TILESIZE= 64
ROWS=15
COLS=15
FPS=60
TITLE="Minesweeper - FII"
LATIME = int(TILESIZE * ROWS)
INALTIME =int(TILESIZE * COLS) 


#procesarea pozelor din ./poze
#numere din celule care indica cati vecini care au bomba are casuta respectiva
numere=[]
for i in range (1,9):
    numere.append(pygame.transform.scale(pygame.image.load(os.path.join("poze", f"Tile{i}.png")), (TILESIZE,TILESIZE)))

c_goala=pygame.transform.scale(pygame.image.load(os.path.join("poze", "TileEmpty.png")), (TILESIZE,TILESIZE))
c_exploded=pygame.transform.scale(pygame.image.load(os.path.join("poze", "TileExploded.png")), (TILESIZE,TILESIZE))
c_flag=pygame.transform.scale(pygame.image.load(os.path.join("poze", "TileFlag.png")), (TILESIZE,TILESIZE))
c_mina=pygame.transform.scale(pygame.image.load(os.path.join("poze", "TileMine.png")), (TILESIZE,TILESIZE))
c_notmina=pygame.transform.scale(pygame.image.load(os.path.join("poze", "TileNotMine.png")), (TILESIZE,TILESIZE))
c=pygame.transform.scale(pygame.image.load(os.path.join("poze", "TileUnknown.png")), (TILESIZE,TILESIZE))

