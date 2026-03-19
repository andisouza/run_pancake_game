import pygame.image

from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_ORANGE, C_GREY, C_BLACK, MENU_OPTION

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/Background/Menu1.png') # Carrega a img
        self.rect = self.surf.get_rect(left=0, top=0) # Cria o retangulo q vai a img
        self.select_sound = pygame.mixer.Sound('./assets/Sons/menuselec.wav')
        self.cloud = pygame.image.load('./assets/Background/Menu2.png').convert_alpha()
        self.cloud_x1 = 0
        self.cloud_x2 = self.cloud.get_width()
        self.cloud_speed = 0.3

    def run(self, ):
        menu_option = 0

        # tocar a música de fundo
        pygame.mixer_music.load('./assets/Sons/song.mp3')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.1)
        
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.window.blit(self.cloud, (self.cloud_x1, 0))
            self.window.blit(self.cloud, (self.cloud_x2, 0))

            self.menu_text(120, "Jump", (C_ORANGE), ((WIN_WIDTH / 2), 200))
            self.menu_text(100, "Pancake", (C_ORANGE), ((WIN_WIDTH / 2), 300))
            
            for i in range(len(MENU_OPTION)):
                if i == menu_option: # colore a seleção de amarelo
                    self.menu_text(20, MENU_OPTION[i], (C_BLACK), ((WIN_WIDTH / 2), 380 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], (C_GREY), ((WIN_WIDTH / 2), 380 + 25 * i))
            
            # MOVIMENTO DAS NUVENS
            self.cloud_x1 -= self.cloud_speed
            self.cloud_x2 -= self.cloud_speed

            # loop infinito
            if self.cloud_x1 <= -self.cloud.get_width():
                self.cloud_x1 = self.cloud.get_width()

            if self.cloud_x2 <= -self.cloud.get_width():
                self.cloud_x2 = self.cloud.get_width()

            pygame.display.flip()

            # verifica eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # fecha a janela
                    quit() # finaliza pygame
                
                # key down / key up
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.select_sound.play()
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    elif event.key == pygame.K_UP:
                        self.select_sound.play()
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    elif event.key == pygame.K_RETURN:  # ENTER
                        return MENU_OPTION[menu_option]
                

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='DejaVu Sans Mono', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)