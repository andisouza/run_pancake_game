import pygame.image

from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_ORANGE, C_WHITE, MENU_OPTION

class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/Background/Menu1.png') # Carrega a img
        self.rect = self.surf.get_rect(left=0, top=0) # Cria o retangulo q vai a img

    def run(self, ):
        # pygame.mixer_music.load('./assets/Sons/song.mp3')
        # pygame.mixer_music.play(-1)
        
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(120, "Jump", (C_ORANGE), ((WIN_WIDTH / 2), 200))
            self.menu_text(100, "Pancake", (C_ORANGE), ((WIN_WIDTH / 2), 300))
            
            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], (C_WHITE), ((WIN_WIDTH / 2), 380 + 25 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # fecha a janela
                    quit() # finaliza pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='DejaVu Sans Mono', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)