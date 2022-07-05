from dataclasses import dataclass

import pygame.image


@dataclass
class Player:
    name: str = ""
    lifes: int = 3
    points: int = 0
    __mesh = pygame.image.load('assets/img/player.png')
    __is_alive: bool = True

    def __get_scaled_mesh__(self):
        scale = self.__mesh.get_size()
        return pygame.transform.scale(self.__mesh, (scale[0] / 2, scale[1] / 2))

    def __is_alive__(self) -> bool:
        return self.__is_alive

    def __event_on_hit__(self):
        if self.lifes == 0:
            self.__is_alive = False
        if self.lifes > 0:
            self.lifes -= 1

    def __event_on_shoot__(self):
        print("Shoot!!")
