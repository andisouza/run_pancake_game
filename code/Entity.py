import pygame.image

from abc import ABC, abstractmethod
from code.Const import WIN_HEIGHT, WIN_WIDTH

class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./assets/Background/' + name + '.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT)) # transforma o tamanho das img
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
    
    @abstractmethod
    def move(self, ):
        pass