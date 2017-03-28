#!/usr/bin/pyhon2.7.9

import abc, pygame, sys
from math import log
from pygame.locals import *
import board
from computer import Ai
from board import Board



class Game:
    def __init__(self, width, ai_turn=False):
        pygame.init()
        self.fps_clock = pygame.time.Clock()

        self.board = Board(width)
        self.ai = Ai(self.board)
        self.ai_turn = ai_turn

    def run(self):
        while not self.handle_events():
            self.board.draw()
            if self.ai_turn:
                self.ai.make_turn()
                self.ai_turn = False
            self.fps_clock.tick(15)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                return True

            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                if self.ai_turn:
                    continue
                x, y = pygame.mouse.get_pos()
                self.ai_turn = self.board.player_move(x, y)


if __name__ == "__main__":
    game = Game(3)
    game.run()