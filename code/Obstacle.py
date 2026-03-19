import pygame
from code.Const import WIN_HEIGHT

class Obstacle():
    def __init__(self, name, position):
        self.name = name

        # TOCO
        if self.name == 'Toco':
            self.surf = pygame.image.load('./assets/Obstaculos/toco.png').convert_alpha()
            self.surf = pygame.transform.scale(self.surf, (70, 70))

        # PASSARO 
        elif self.name == 'Passaro':
            self.frames = [
                pygame.image.load(f'./assets/Obstaculos/passaro-{i}.png').convert_alpha()
                for i in range(1, 4)
            ]
            self.frame_index = 0
            self.counter = 0
            self.animation_speed = 0.2
            self.surf = self.frames[self.frame_index]

        # POSIÇÃO
        if self.name == 'Toco':
            y = WIN_HEIGHT - 50 - self.surf.get_height()
        else:  # Passaro
            y = WIN_HEIGHT - 200  # ajusta depois visualmente

        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 5

    def move(self):
        # movimento padrão
        self.rect.x -= self.speed

        # animação do pássaro
        if self.name == 'Passaro':
            self.counter += self.animation_speed
            if self.counter >= 1:
                self.counter = 0
                self.frame_index = (self.frame_index + 1) % len(self.frames)
                self.surf = self.frames[self.frame_index]

    def off_screen(self):
        return self.rect.right < 0