import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Menu import Menu
from code.Level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.mixer.init()

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()
            
            if menu_return == MENU_OPTION[0]:
                while True:
                    level = Level(self.window)
                    result = level.run()

                    if result == "game_over":
                        action = level.game_over_screen()

                        if action == "restart":
                            continue
                        elif action == "menu":
                            break
            else:
                pygame.quit()
                quit()




    def jump(self, ):
        pass

    def dodge(self, ):
        pass
