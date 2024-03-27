from constants import *
from graphics import Line, Point


class Cell:
    def __init__(self, x1, y1, x2, y2, window=None):
        self.north_wall = True
        self.south_wall = True
        self.east_wall = True
        self.west_wall = True
        self._window = window
        # (x1, y1) -> top-left point
        self._x1 = x1
        self._y1 = y1
        # (x2, y2) -> bottom-right point
        self._x2 = x2
        self._y2 = y2

    def draw(self):
        if self._window is None:
            return
        if self.north_wall:
            self._window.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)),
                WALL_COLOR,
            )
        if self.south_wall:
            self._window.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2)),
                WALL_COLOR,
            )
        if self.east_wall:
            self._window.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)),
                WALL_COLOR,
            )
        if self.west_wall:
            self._window.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2)),
                WALL_COLOR,
            )

    def center_point(self):
        return Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)

    def draw_move(self, other, undo=False):
        if self._window is None:
            return
        self._window.draw_line(
            Line(self.center_point(), other.center_point()),
            UNDO_COLOR if undo else PATH_COLOR,
        )
