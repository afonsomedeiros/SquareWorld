from pygame import display, time, init, event, QUIT, display, key, K_SPACE

from Ball import Ball
from Player import Player
from Block import Block
from Restart import Restart

class Game():
    RESOLUTION = (1024, 640)
    screen = display.set_mode(RESOLUTION)
    clock = time.Clock()
    running = True
    round = 1

    def __init__(self, player: Player, ball: Ball, blocks: list[Block], restart: Restart) -> None:
        init()
        self.player = player
        self.ball = ball
        self.blocks = blocks
        self.restart = restart

        self.player.set_surface(self.screen)
        self.ball.set_surface(self.screen)

        self.player.set_initial_pos()
        self.ball.set_initial_pos()

        self.loop()

    def reset(self, not_removed):
        self.ball.lose = False
        self.ball.set_initial_pos()
        self.ball.removed = 0 if not_removed == False else self.ball.removed
        self.player.set_initial_pos()
        for block in self.blocks:
            self.blocks[self.blocks.index(block)].colision = True
            self.blocks[self.blocks.index(block)].change_color()

    def loop(self):
        while self.running:
            for ev in event.get():
                if ev.type == QUIT:
                    self.running = False
                if self.ball.lose == True and key.get_pressed()[K_SPACE]:
                    self.reset(False)            

            self.screen.fill("black")

            if self.ball.lose == False:
                for block in self.blocks:
                    if block.colision == True:
                        block.set_surface(self.screen)
                        block.set_initial_pos()
                        block.draw()
                        block.check_colision(self.ball)
                self.player.draw()
                self.ball.draw()
            else:
                self.restart.show(self.screen, self.ball.removed, self.round)
            
            if len(self.blocks) == int(self.ball.removed / self.round):
                self.round += 1
                self.ball.speed += 2
                self.reset(True)

            self.player.get_key_pressed()
            self.player.check_colision(self.ball)
            
            self.ball.move()

            display.flip()
            self.clock.tick(60)

