import pygame
from setari import *

class UserInterface:
    
    def __init__(self, screen):
        self.screen = screen
        
        # Dimensiunile ecranului (inclusiv stats bar)
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        
        # gunoaie de fonturi :/
        self.font_large = pygame.font.Font(None, 72)
        self.font_medium = pygame.font.Font(None, 40)
        self.font_small = pygame.font.Font(None, 30)
        self.font_tiny = pygame.font.Font(None, 24)
        
        # un array de butoane
        self.butoane_meniu = {}
        
    def draw_home_screen(self):
        """HOME SCREEN - MENIU CENTRAT"""
        self.screen.fill((26, 26, 46))
        
        # Titlul - centrat pe ecran
        titlu = self.font_large.render("MINESWEEPER", True, GREEN)
        titlu_rect = titlu.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 150))
        self.screen.blit(titlu, titlu_rect)
        
        # Subtitlu
        subtitlu = self.font_small.render("Select Difficulty", True, (236, 240, 241))
        subtitlu_rect = subtitlu.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 80))
        self.screen.blit(subtitlu, subtitlu_rect)
        
        # Butoane dificultate - centrate vertical
        difficulties = [
            ("EASY", "easy", "15% mine", -20),
            ("MEDIUM", "medium", "20% mine", 60),
            ("HARD", "hard", "25% mine", 140)
        ]
        
        self.butoane_meniu = {}
        
        for label, diff_key, info, y_offset in difficulties:
            # butonul principal - centrat pe ecran
            button_rect = pygame.Rect(
                self.screen_width // 2 - 200, 
                self.screen_height // 2 + y_offset, 
                400, 
                60
            )
            
            # hover effectul
            mouse_pos = pygame.mouse.get_pos()
            if button_rect.collidepoint(mouse_pos):
                pygame.draw.rect(self.screen, (52, 152, 219), button_rect, border_radius=10)
            else:
                pygame.draw.rect(self.screen, (52, 58, 70), button_rect, border_radius=10)
            
            pygame.draw.rect(self.screen, (88, 96, 115), button_rect, 2, border_radius=10)
            
            # TEXTUL DIN BUTTON
            text = self.font_medium.render(label, True, WHITE)
            text_rect = text.get_rect(center=(button_rect.centerx, button_rect.centery - 8))
            self.screen.blit(text, text_rect)
            
            # TEXT INFO
            info_text = self.font_tiny.render(info, True, (149, 165, 166))
            info_rect = info_text.get_rect(center=(button_rect.centerx, button_rect.centery + 18))
            self.screen.blit(info_text, info_rect)
            self.butoane_meniu[diff_key] = button_rect
        
        pygame.display.flip()
    
    
    def draw_timer_and_stats(self, timp, mines):
        """Deseneaza overlay pentru timer si statistici

        Args:
            timp (int): timpul pe care il ai
            mines (int): numarul de mine ramase
        """
        # fundal
        stats_bg = pygame.Surface((self.screen_width, 60))
        stats_bg.fill((26, 26, 46))
        self.screen.blit(stats_bg, (0, 0))
        
        # K mines
        mines_text = f"{mines}"
        mines_surf = self.font_medium.render(mines_text, True, (52, 152, 219))
        self.screen.blit(mines_surf, (30, 15))
        
        # timer - centrat
        timer_text = f"{timp}s"
        timer_surf = self.font_medium.render(timer_text, True, (46, 204, 113))
        timer_rect = timer_surf.get_rect(center=(self.screen_width // 2, 30))
        self.screen.blit(timer_surf, timer_rect)
        
        # hint restart
        restart_text = "R - Restart"
        restart_surf = self.font_small.render(restart_text, True, (149, 165, 166))
        restart_rect = restart_surf.get_rect(right=self.screen_width - 30, centery=30)
        self.screen.blit(restart_surf, restart_rect)
    
    def show_endframe(self, message_type, timp):
        """
        Afiseaza overlay-ul de final (win/lose)
        Args:
            message_type (str): "win" sau "lose"
            timp (int): timpul(in secunde)
        Returns:
            str: "restart", "menu", sau "quit"
        """
        # overlay - FIX: Include toata inaltimea ecranului (cu stats bar)
        overlay = pygame.Surface((self.screen_width, self.screen_height))
        overlay.set_alpha(200)
        overlay.fill((26, 26, 46))
        self.screen.blit(overlay, (0, 0))
        
        if message_type == "win":
            message = "VICTORY!"
            color = GREEN
            sub_message = f"Completed in {timp} seconds!"
        else:  # "lose"
            message = "GAME OVER"
            color = RED
            sub_message = "Better luck next time!"
        
        # Mesaj principal - centrat pe ecran
        text = self.font_large.render(message, True, color)
        text_rect = text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 50))
        self.screen.blit(text, text_rect)
        
        # sub-mesaj
        sub_text = self.font_medium.render(sub_message, True, (236, 240, 241))
        sub_rect = sub_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 20))
        self.screen.blit(sub_text, sub_rect)
        
        # lista de optiuni
        restart_text = "R - Restart  |  ESC - Menu  |  Q - Quit"
        restart = self.font_small.render(restart_text, True, (149, 165, 166))
        restart_rect = restart.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 80))
        self.screen.blit(restart, restart_rect)
        
        pygame.display.flip()
        
        # input utilizator
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        return "restart"
                    elif event.key == pygame.K_ESCAPE:
                        return "menu"
                    elif event.key == pygame.K_q:
                        return "quit"
            
            pygame.time.Clock().tick(FPS)
        
        return "quit"
    
    def check_menu_click(self, mouse_pos):
        """
        Verifica daca s a dat click la ceva in meniu
        Returns:
            str: dificultatea selectata sau None
        """
        for diff_key, button_rect in self.butoane_meniu.items():
            if button_rect.collidepoint(mouse_pos):
                return diff_key
        return None
    
    def draw_custom_screen(self):
        """Placeholder pentru custom menu"""
        self.screen.fill((26, 26, 46))
        
        text = self.font_large.render("Custom Mode - Coming Soon", True, WHITE)
        text_rect = text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
        self.screen.blit(text, text_rect)
        
        hint = self.font_small.render("Press ESC to return", True, (149, 165, 166))
        hint_rect = hint.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 60))
        self.screen.blit(hint, hint_rect)
        
        pygame.display.flip()