#!/usr/bin/pyhon2.7.9

import abc
import pygame
import pygame.locals


def player_marker(x_player):
    return "X" if x_player else "O"


def check_win(markers, x_player, width):
    win = [player_marker(x_player)] * width
    seq = range(width)

    def marker(xx, yy):
        return markers[xx + yy * width]

    for x in seq:
        row = [marker(x, y) for y in seq]
        if row == win:
            return True

    for y in seq:
        col = [marker(x, y) for x in seq]
        if col == win:
            return True

    diagonal1 = [marker(i, i) for i in seq]
    diagonal2 = [marker(i, abs(i - 2)) for i in seq]
    if diagonal1 == win or diagonal2 == win:
        return True


class abstractBoard(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def draw(self, w):
        pass

    @abc.abstractmethod
    def draw_net(self):
        pass


class Board(abstractBoard):
    def __init__(self, width):
        self.w = width
        self.surface = pygame.display.set_mode((width * 100, width * 100), 0, 32)
        pygame.display.set_caption('Tic-tac-toe')

        pygame.font.init()
        font_path = pygame.font.match_font('arial')
        self.font = pygame.font.Font(font_path, 48)

        self.markers = [None] * width * width

    def draw(self, *args):
        background = (0, 0, 0)
        self.surface.fill(background)
        self.draw_net()
        self.draw_markers()
        self.draw_score()
        for drawable in args:
            drawable.draw_on(self.surface)

        pygame.display.update()

    def draw_net(self):
        color = (255, 255, 255)
        width = self.surface.get_width()
        for i in range(1, self.w):
            pos = width / self.w * i
            pygame.draw.line(self.surface, color, (0, pos), (width, pos), 1)
            pygame.draw.line(self.surface, color, (pos, 0), (pos, width), 1)

    def player_move(self, x, y):
        cell_size = self.surface.get_width() / self.w
        x /= cell_size
        y /= cell_size
        if not self.markers[x + y * self.w]:
            self.markers[x + y * self.w] = player_marker(True)
            return True
        return False

    def draw_markers(self):
        box_side = self.surface.get_width() / self.w
        for x in range(self.w):
            for y in range(self.w):
                marker = self.markers[x + y * self.w]
                if not marker:
                    continue
                center_x = x * box_side + box_side / 2
                center_y = y * box_side + box_side / 2

                self.draw_text(self.surface, marker, (center_x, center_y))

    def draw_text(self, surface, text, center, color=(180, 180, 180)):
        text = self.font.render(text, True, color)
        rect = text.get_rect()
        rect.center = center
        surface.blit(text, rect)

    def draw_score(self):
        if check_win(self.markers, True, self.w):
            score = u"Wygrales(as)"
        elif check_win(self.markers, True, self.w):
            score = u"Przegraes(as)"
        elif None not in self.markers:
            score = u"Remis!"
        else:
            return

        i = self.surface.get_width() / 2
        self.draw_text(self.surface, score, center=(i, i), color=(255, 26, 26))
