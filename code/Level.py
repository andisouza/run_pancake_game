import pygame
import sys
import random

from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Player import Player
from code.Obstacle import Obstacle
from code.Const import C_ORANGE

class Level:
    def __init__(self, window):
        self.window = window
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Lv1Bg'))  # fundo
        self.player = Player((100, 50))  # posição inicial
        self.entity_list.append(self.player)
        self.spawn_timer = 0
        self.spawn_delay = random.randint(50, 150)  # quanto maior, mais espaçado (60 ~ 1 segundo)
        self.last_obstacle = None
        self.game_time = 0
        self.score = 0
        self.hit_sound = pygame.mixer.Sound('./assets/Sons/hit.mp3')
        self.hit_sound.set_volume(0.7)
        self.game_over = False
        self.menu_option = 0  # 0 = restart, 1 = menu

    def run(self, ):
        # tocar a música de fundo
        pygame.mixer_music.load('./assets/Sons/song.mp3')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            self.window.fill((0, 0, 0))
            if not self.game_over:
                self.game_time += 1
                self.score += 0.1

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                if not self.game_over:
                    ent.move()

            for ent in self.entity_list:
                if isinstance(ent, Obstacle):

                   # hitbox do player muda quando abaixa
                    if self.player.is_dodging:
                        player_rect = self.player.rect.inflate(-40, -10)
                    else:
                        player_rect = self.player.rect.inflate(-20, -20)

                    obstacle_rect = ent.rect.inflate(-10, -10)

                    if player_rect.colliderect(obstacle_rect) and not self.game_over:
                        self.hit_sound.play()
                        pygame.time.delay(300)
                        self.game_over = True
            
            # SPAWN DE OBSTÁCULOS
            self.spawn_timer += 1

            if not self.game_over and self.spawn_timer >= self.spawn_delay:

                # escolhe tipo com peso
                if random.random() < 0.7:
                    tipo = 'Toco'
                else:
                    tipo = 'Passaro'

                # evita repetição chata
                if tipo == self.last_obstacle:
                    if random.random() < 0.7:
                        tipo = 'Toco' if tipo == 'Passaro' else 'Passaro'

                # salva último
                self.last_obstacle = tipo

                # cria obstáculo
                if tipo == 'Toco':
                    pos_y = 500
                else:
                    pos_y = 400

                obstacle = Obstacle(tipo, (1100, pos_y))

                # aumenta velocidade com o tempo
                obstacle.speed += self.game_time // 500

                self.entity_list.append(obstacle)

                # reseta tempo
                self.spawn_timer = 0
                base_delay = max(40, 180 - self.game_time // 10)
                self.spawn_delay = random.randint(base_delay, base_delay + 60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if not self.game_over:
                        if event.key == pygame.K_UP:
                            self.player.jump()
                    else:
                        if event.key == pygame.K_DOWN:
                            self.menu_option = (self.menu_option + 1) % 2
                        elif event.key == pygame.K_UP:
                            self.menu_option = (self.menu_option - 1) % 2
                        elif event.key == pygame.K_RETURN:
                            if self.menu_option == 0:
                                return "restart"
                            else:
                                return "menu"

            # REMOVE OBSTÁCULOS QUE SAÍRAM DA TELA
            self.entity_list = [
                ent for ent in self.entity_list
                if not hasattr(ent, 'off_screen') or not ent.off_screen()
            ]

            font = pygame.font.SysFont('Arial', 30)
            score_surf = font.render(f"Score: {int(self.score)}", True, (255, 255, 255))
            self.window.blit(score_surf, (900, 20))

            if self.game_over:
                # overlay escuro
                overlay = pygame.Surface((1100, 600))
                overlay.set_alpha(120)
                overlay.fill((0, 0, 0))
                self.window.blit(overlay, (0, 0))

                # caixa branca com transparência (mais suave)
                box = pygame.Surface((400, 250), pygame.SRCALPHA)
                pygame.draw.rect(
                    box,
                    (255, 255, 255, 180),  # transparência melhor
                    (0, 0, 400, 250),
                    border_radius=20
                )

                pygame.draw.rect(
                    box,
                    (200, 200, 200),
                    (0, 0, 400, 250),
                    width=2,
                    border_radius=20
)
                # centraliza a caixa
                box_rect = box.get_rect(center=(1100 // 2, 600 // 2))
                self.window.blit(box, box_rect)

                # fontes
                font_big = pygame.font.SysFont('DejaVu Sans Mono', 40)
                font_small = pygame.font.SysFont('DejaVu Sans Mono', 25)

                # centro da tela
                center_x = 1100 // 2
                center_y = 600 // 2

                # título centralizado
                title = font_big.render("GAME OVER", True, C_ORANGE)
                title_rect = title.get_rect(center=(center_x, center_y - 60))
                self.window.blit(title, title_rect)

                # opções centralizadas
                options = ["RESTART", "MENU"]

                for i, option in enumerate(options):
                    color = (0, 0, 0) if i == self.menu_option else (120, 120, 120)

                    text = font_small.render(option, True, color)
                    text_rect = text.get_rect(center=(center_x, center_y + i * 40))

                    self.window.blit(text, text_rect)

            pygame.display.flip()