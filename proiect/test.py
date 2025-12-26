import pygame
pygame.init()

# Creează fereastră
screen = pygame.display.set_mode((740, 740))
pygame.display.set_caption("Minesweeper Test")

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Culoare de fundal
    screen.fill((200, 200, 200))
    pygame.display.flip()

pygame.quit()