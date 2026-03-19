import pygame
import sys

from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Player import Player

class Level:
    def __init__(self, window):
        self.window = window
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Lv1Bg'))  # fundo
        self.player = Player((100, 50))  # posição inicial
        self.entity_list.append(self.player)

    def run(self, ):
        # tocar a música de fundo
        pygame.mixer_music.load('./assets/Sons/song.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player.jump()
                    
            pygame.display.flip()
