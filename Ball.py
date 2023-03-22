from pygame import draw, Vector2, Surface

from GameObject import GameObject
from DIRECTIONS import Directions
from COLORS import Colors

class Ball(GameObject):
    gravity = True
    speed = 5
    radius = 20
    direction = Directions.LEFT
    lose = False
    removed = 0

    def set_initial_pos(self) -> None:
        self._pos = Vector2(self.surface.get_width() * 0.55, self.surface.get_height() / 2)

    def draw(self):
        draw.circle(self.surface, Colors.RED, self._pos, self.radius)

    def set_surface(self, surface: Surface):
        self.surface = surface

    def move(self):
        self.change_direction_or_gravity()
        self.move_x()
        self.move_y()

    def move_x(self):
        if self.direction == Directions.LEFT:
            self._pos.x += self.speed
        else:
            self._pos.x -= self.speed

    def move_y(self):
        if self.gravity:
            self._pos.y += self.speed
        else:
            self._pos.y -= self.speed

    def change_direction_or_gravity(self):
        if (self._pos.x - self.radius) <= 0:
            self.direction = Directions.LEFT
        elif (self._pos.x + self.radius) >= self.surface.get_width():
            self.direction = Directions.RIGHT
        elif (self._pos.y - self.radius) <= 0:
            self.gravity = True
        if (self._pos.y + self.radius) >= self.surface.get_height():
            self.lose = True

