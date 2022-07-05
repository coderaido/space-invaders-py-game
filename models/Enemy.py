from dataclasses import dataclass

import pygame.image
from pygame.surface import SurfaceType, Surface


@dataclass
class Enemy:
    health: float
    name: str
    points: float
    velocity: float
    mesh:Surface | SurfaceType