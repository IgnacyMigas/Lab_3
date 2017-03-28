#!/usr/bin/pyhon2.7.9

import logging
import random
from  board import player_marker

logging_format = '%(asctime)s %(levelname)-7s | %(module)s.%(funcName)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=logging_format, datefmt='%H:%M:%S')
logging.getLogger().setLevel(logging.INFO)


class Ai(object):
    def __init__(self, board):
        self.board = board

    def make_turn(self):
        if not None in self.board.markers:
            return
        logging.debug("Plansza: %s" % self.board.markers)
        move = self.next_move(self.board.markers)
        self.board.markers[move] = player_marker(False)

    @classmethod
    def next_move(cls, markers):
        moves = cls.score_moves(markers, False)
        score, move = max(moves, key=lambda m: m[0])
        logging.info("Dostepne ruchy: %s", moves)
        logging.info("Wybrany ruch: %s %s", move, score)
        return move

    @classmethod
    def score_moves(cls, markers, x_player):
        available_moves = (i for i, m in enumerate(markers) if m is None)
        print random.randint(0, len(markers) - 1)
        for move in available_moves:
            yield random.randint(0, 20), move
