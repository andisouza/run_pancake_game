from code.Background import Background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Lv1Bg1':
                list_bg = []

                for i in range(3): # juntando todas as partes do background
                    list_bg.append(Background(f'Lv1Bg{i}', (0,0)))
                return list_bg