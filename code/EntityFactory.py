from code.Background import Background
from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Lv1Bg':
                list_bg = []

                for i in range(1, 4): # juntando todas as partes do background
                    list_bg.append(Background(f'Lv1Bg{i}', (0,0)))
                    list_bg.append(Background(f'Lv1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player':
                return Player((10, 250))