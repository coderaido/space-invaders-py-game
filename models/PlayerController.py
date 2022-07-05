from dataclasses import dataclass

import pygame
from pygame.surface import Surface, SurfaceType

from models.Coordinates import Coordinates
from models.Player import Player


@dataclass
class PlayerController:
    __playerPosition: Coordinates
    player: Player = Player()
    __max_character_movement: float = 15.0

    def __init__(self, coords: Coordinates):
        img_scale = self.player.__get_scaled_mesh__().get_size()
        self.__playerPosition = Coordinates((coords.xPosition / 2) - (img_scale[0]/2), coords.yPosition - (img_scale[1] + 20))

    def __get_player_position__(self) -> Coordinates:
        return self.__playerPosition

    def __change_player_position__(self, delta_time, screen_size: tuple):
        coords: Coordinates = self.__get_player_position__()
        keys = pygame.key.get_pressed()
        screen_size_x = screen_size[0]

        if coords.xPosition > 0:
            if keys[pygame.K_LEFT]:
                coords.xPosition -= round(self.__max_character_movement * delta_time, 3)
        if coords.xPosition < (screen_size_x - self.player.__get_scaled_mesh__().get_size()[0]):
            if keys[pygame.K_RIGHT]:
                coords.xPosition += round(self.__max_character_movement * delta_time, 3)

    def __print_player__(self, screen: Surface | SurfaceType):
        coordinates = self.__get_player_position__()
        screen.blit(self.player.__get_scaled_mesh__(), (coordinates.xPosition, coordinates.yPosition))

    def __spacebar_event(self):
        pass

    def set_player_position(self, coords: Coordinates):
        self.__playerPosition = coords
