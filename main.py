import sys

import pygame
from pygame.event import Event

from models.Coordinates import Coordinates
from models.PlayerController import PlayerController

pygame.init()

FPS = 60


def start_player_controller():
    global playerController
    player_start_coords = Coordinates(screen_size[0], screen_size[1] - 10)
    playerController = PlayerController(player_start_coords)


if __name__ == '__main__':
    clock = pygame.time.Clock()
    t = pygame.time.get_ticks()
    # deltaTime in seconds.
    dt = clock.tick(FPS) / 1000
    size = width, height = 500, 750
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Space Invaders - By CodeRaido")
    screen_size = screen.get_size();
    end_line: pygame.Rect = pygame.Rect(0, size[1]-20, screen_size[1], 2)

    start_player_controller()
    run = True
    lastEvent: Event
    while run:

        pygame.display.flip()
        screen.fill(black)
        playerController.__print_player__(screen)
        pygame.draw.rect(screen, pygame.Color('green'), end_line)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            playerController.__change_player_position__(dt, size)

        pygame.display.update()
