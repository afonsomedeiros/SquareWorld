from pygame import Vector2, Surface
from abc import ABC


class GameObject(ABC):
    _pos: Vector2 = ()
    surface: Surface = None

    def draw(self):
        ...

    def set_initial_pos(self) -> None:
        ...

    def set_surface(self, surface: Surface):
        ...

    def check_colision(self):
        ...
