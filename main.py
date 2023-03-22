from Ball import Ball
from Player import Player
from Block import Block
from Game import Game
from Restart import Restart


def generate_blocks():
    blocks = []
    x, y, w, h, s = 20, 10, 50, 15, 0
    for i in range(0, 72):
        if i != 0:
            s = 5
        if i % 18 == 0 and i > 0:
            y += h + s
            s = 0
            x = 20
        blocks.append(Block(x, y, w, h, s))
        x += w + s
    return blocks


def main():
    player = Player()
    ball = Ball()
    restart = Restart()
    blocks = generate_blocks()
    game = Game(player, ball, blocks, restart)
    game.loop()


if __name__ == '__main__':
    main()