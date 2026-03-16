import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu

class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run
            pass

    def jump(self, ):
        pass

    def dodge(self, ):
        pass

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit() # close window
#             quit() # end pygame