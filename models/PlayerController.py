from dataclasses import dataclass

import pygame

from models.Coordinates import Coordinates
from models.Player import Player


@dataclass
class PlayerController:
    __playerPosition: Coordinates = Coordinates(xPosition=50, yPosition=50)
    player: Player = Player(name="Player Name", lifes=3)
    mesh: pygame.Rect = pygame.Rect(0, 0, 20, 20)
    __max_character_movement: float = 5.0

    def __get_player_position__(self) -> Coordinates:
        return self.__playerPosition

    def __change_player_position__(self, event, delta_time, screen_size: tuple):
        coords: Coordinates = self.__get_player_position__()
        keys = pygame.key.get_pressed()
        screen_size_x = screen_size[0]
        if coords.xPosition > self.mesh.x:
            if keys[pygame.K_LEFT]:
                coords.xPosition -= round(self.__max_character_movement * delta_time, 3)
        if coords.xPosition < (screen_size_x - 20):
            if keys[pygame.K_RIGHT]:
                coords.xPosition += round(self.__max_character_movement * delta_time, 3)
        if keys[pygame.K_UP]:
            coords.yPosition -= self.__max_character_movement * delta_time
        if keys[pygame.K_DOWN]:
            coords.yPosition += self.__max_character_movement * delta_time

        self.__update_mesh_coords__()

    def __update_mesh_coords__(self):
        self.mesh.x = self.__get_player_position__().xPosition
        self.mesh.y = self.__get_player_position__().yPosition

    def __print_player__(self, screen):
        pygame.draw.rect(screen, pygame.Color('red'), self.mesh)

    def __spacebar_event(self):
        pass
