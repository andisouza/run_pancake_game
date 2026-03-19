import pygame
from code.Entity import Entity
from code.Const import WIN_HEIGHT

class Player(Entity):
    def __init__(self, position: tuple):
        size = (90, 90)
        # carregar os 4 frames
        self.frames = [
            pygame.transform.scale(
                pygame.image.load(f'./assets/Panqueca/{f}').convert_alpha(), size
            )
            for f in ('Pq1.png', 'Pq2.png', 'Pq3.png', 'Pq4.png')
        ]
        # frame abaixado
        self.dodge_frame = pygame.transform.scale(
            pygame.image.load('./assets/Panqueca/Pq5.png').convert_alpha(), size
        )

        self.frame_index = 0
        self.surf = self.frames[self.frame_index]
        self.rect = self.surf.get_rect(left=position[0], top=position[1])

        self.counter = 0
        self.animation_speed = 0.2
        self.y_vel = 0
        self.on_ground = True
        self.is_dodging = False

    def move(self):
        keys = pygame.key.get_pressed()
        self.is_dodging = keys[pygame.K_DOWN]

        # abaixado
        if self.is_dodging:
            self.surf = self.dodge_frame
        else:
            # corrida normal
            self.counter += self.animation_speed
            if self.counter >= 1:
                self.counter = 0
                self.frame_index = (self.frame_index + 1) % len(self.frames)
                self.surf = self.frames[self.frame_index]

        # gravidade e pulo
        self.y_vel += 1
        self.rect.y += self.y_vel

        # chão
        if self.rect.bottom >= WIN_HEIGHT - 80:
            self.rect.bottom = WIN_HEIGHT - 80
            self.y_vel = 0
            self.on_ground = True

    def jump(self):
        if self.on_ground and not self.is_dodging:
            self.y_vel = -15
            self.on_ground = False