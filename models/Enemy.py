from dataclasses import dataclass


@dataclass
class Enemy:
    health: float
    name: str
    points: float
    velocity: float
    