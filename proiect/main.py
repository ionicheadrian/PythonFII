import pygame
from setari import *
from game_engine import Game_engine
from ui import UserInterface

class MinesweeperApp:
    def __init__(self):
        pygame.init()
        # Maresc inaltimea ferestrei pentru stats bar
        self.screen = pygame.display.set_mode((LATIME, INALTIME + 60))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Managers
        self.ui = UserInterface(self.screen)
        self.game = None
        
        # State
        self.state = "menu"  # "menu", "playing", "custom"
    
    def run(self):
        """Main loop al aplicatiei"""
        while self.running:
            if self.state == "menu":
                self.run_menu()
            elif self.state == "playing":
                self.run_game()
            elif self.state == "custom":
                self.run_custom_menu()
        
        pygame.quit()
    
    def run_menu(self):
        """Loop pentru meniu"""
        while self.state == "menu" and self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    selected_diff = self.ui.check_menu_click(event.pos)
                    
                    if selected_diff == "custom":
                        self.state = "custom"
                    elif selected_diff:
                        # Start joc cu dificultatea selectata
                        self.game = Game_engine(selected_diff)
                        self.game.new_game()
                        self.state = "playing"
            
            self.ui.draw_home_screen()
            self.clock.tick(FPS)
    
    def run_custom_menu(self):
        """Loop pentru meniul custom (TODO: implement custom settings)"""
        while self.state == "custom" and self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.state = "menu"
            
            self.ui.draw_custom_screen()
            self.clock.tick(FPS)
    
    def run_game(self):
        """Loop pentru joc activ"""
        # Offset pentru stats bar
        board_offset_y = 60
        
        while self.state == "playing" and self.running:
            # Update timer
            self.game.update_timer()
            
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.state = "menu"
                
                # Mouse clicks
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    cell_coords = self.game.get_cellpos(x, y - board_offset_y)
                    
                    if cell_coords:
                        row, col = cell_coords
                        
                        if event.button == 1:  # Left click
                            result = self.game.handle_click(int(event.button), row, col)
                            
                            if result == "lose":
                                action = self.ui.show_endframe("lose", self.game.timp)
                                self.handle_endgame_action(action)
                            
                            elif result == "win":
                                action = self.ui.show_endframe("win", self.game.timp)
                                self.handle_endgame_action(action)
                        
                        elif event.button == 3:
                            result = self.game.handle_click(int(event.button), row, col)
                            
                            if result == "win":
                                action = self.ui.show_endframe("win", self.game.timp)
                                self.handle_endgame_action(action)
                
                # Keyboard shortcuts
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.game.new_game()
                    elif event.key == pygame.K_ESCAPE:
                        self.state = "menu"
                    elif event.key == pygame.K_w:
                        self.game.necuratu()
            
            # Drawing - FIX: Trec board_offset_y ca parametru
            self.draw_game(board_offset_y)
            pygame.display.flip()
            self.clock.tick(FPS)
    
    def draw_game(self, board_offset_y):
        """Deseneaza starea curenta a jocului"""
        self.screen.fill((200, 200, 74))
        
        # Desenez stats bar-ul sus
        self.ui.draw_timer_and_stats(self.game.timp, self.game.mines)
        
        # Desenez board-ul sub stats bar
        self.game.board.draw()
        self.screen.blit(self.game.board.board_surface, (0, board_offset_y))
    
    def handle_endgame_action(self, action):
        """Gestioneaza actiunea dupa endgame"""
        if action == "restart":
            self.game.new_game()
        elif action == "menu":
            self.state = "menu"
            self.game = None
        elif action == "quit":
            self.running = False


if __name__ == "__main__":
    app = MinesweeperApp()
    app.run()