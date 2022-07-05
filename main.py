import sys

import pygame
from pygame.event import Event

from models.PlayerController import PlayerController

pygame.init()

FPS = 60

if __name__ == '__main__':
    clock = pygame.time.Clock()
    t = pygame.time.get_ticks()
    # deltaTime in seconds.
    dt = clock.tick(FPS) / 1000
    size = width, height = 500, 500
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)
    playerController = PlayerController()
    run = True
    updatePosition = True
    lastEvent: Event
    while run:

        pygame.display.flip()
        screen.fill(black)
        playerController.__print_player__(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            playerController.__change_player_position__(event, dt, size)

        pygame.display.update()
