from pygame import draw, Vector2, Surface, Rect, mixer
from random import choice

from GameObject import GameObject
from Ball import Ball
from COLORS import Colors

class Block(GameObject):
    colors = [Colors.BLUE, Colors.GREEN, Colors.WHITE]
    mix = mixer
    def __init__(self, x, y, width, height, space) -> None:
        self._x = x
        self._y = y
        self.width = width
        self.height = height
        self.space = space
        self.change_color()
        self.colision = True
        self.mix.init()

    def play_audio(self):
        self.mix.music.play()
    
    def set_initial_pos(self) -> None:
        self._pos = Vector2(self._x, self._y)

    def draw(self):
        draw.rect(self.surface, self.color, Rect(self._pos.x + self.space, self._y, self.width, self.height))

    def set_surface(self, surface: Surface):
        self.surface = surface

    def change_color(self):
        self.color = choice(self.colors)


    def check_colision(self, gameObject: Ball):
        if (gameObject._pos.y - gameObject.radius) <= (self._y + self.height) and self.colision == True:
            if (
                (gameObject._pos.y - gameObject.radius) <= (self._y + self.height) and
                (
                    int(gameObject._pos.x + gameObject.radius) in range(int(self._pos.x), int(self._pos.x + self.width)) or
                    int(gameObject._pos.x - gameObject.radius) in range(int(self._pos.x), int(self._pos.x + self.width))
                )
            ):
                self.color = Colors.BLACK
                self.colision = False
                gameObject.gravity = True
                gameObject.removed += 1
                self.mix.music.load("som.mp3")
                self.play_audio()
