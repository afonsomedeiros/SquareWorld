from pygame import draw, Vector2, Surface, Rect, key, K_LEFT, K_RIGHT, mixer

from GameObject import GameObject
from Ball import Ball
from COLORS import Colors

class Player(GameObject):
    _y = 600
    width = 200
    height = 25
    mix = mixer

    def __init__(self) -> None:
        self.mix.init()

    def set_initial_pos(self) -> None:
        self._pos = Vector2(self.surface.get_width() * 0.55, self.surface.get_height() * 0.1)

    def draw(self):
        draw.rect(self.surface, Colors.YELLOW, Rect(self._pos.x, self._y, self.width, self.height))

    def set_surface(self, surface: Surface):
        self.surface = surface

    def get_key_pressed(self):
        keys = key.get_pressed()
        if keys[K_RIGHT] and (self._pos.x + self.width) < self.surface.get_width():
            self._pos.x += 10
        if keys[K_LEFT] and self._pos.x > 0:
            self._pos.x -= 10

    def check_colision(self, gameObject: Ball):
        if (gameObject._pos.y + gameObject.radius) >= 600:
            if (
                (gameObject._pos.y + gameObject.radius) == 600 and
                (
                    int(gameObject._pos.x + gameObject.radius) in range(int(self._pos.x), int(self._pos.x + self.width)) or
                    int(gameObject._pos.x - gameObject.radius) in range(int(self._pos.x), int(self._pos.x + self.width))
                )
            ):
                gameObject.gravity = False
                self.mix.music.load("som2.mp3")
                self.play_audio()

    def play_audio(self):
        self.mix.music.play()
