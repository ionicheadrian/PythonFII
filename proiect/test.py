import pygame
from componente import Board

n = 12

def save_board_to_file(board, dif, filename="board.txt"):
    with open(filename, "a") as f:  # "a" = append
        f.write(f"{dif}\n")
        for row in board.board_list:
            f.write(" ".join([str(cell.type) for cell in row]) + "\n")
        f.write("\n\n")

dif = "easy"

for i in range(n + 1):
    if i % 4 == 0 and i != 0:  # Schimbă dificultatea la fiecare 4 iterații
        if dif == "easy":
            dif = "medium"
        elif dif == "medium":
            dif = "hard"
    
    board = Board(dif)
    save_board_to_file(board, dif)

print(f"Salvat {n+1} board-uri în board.txt")