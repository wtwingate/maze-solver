from constants import *
from graphics import Line, Point


class Cell:
    def __init__(self, x1, y1, x2, y2, window=None):
        self.north_wall = True
        self.south_wall = True
        self.east_wall = True
        self.west_wall = True
        self.__window = window
        # (x1, y1) -> top-left point
        self.__x1 = x1
        self.__y1 = y1
        # (x2, y2) -> bottom-right point
        self.__x2 = x2
        self.__y2 = y2

    def draw(self):
        if self.north_wall:
            self.__window.draw_line(
                Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)),
                WALL_COLOR,
            )
        if self.south_wall:
            self.__window.draw_line(
                Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)),
                WALL_COLOR,
            )
        if self.east_wall:
            self.__window.draw_line(
                Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)),
                WALL_COLOR,
            )
        if self.west_wall:
            self.__window.draw_line(
                Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)),
                WALL_COLOR,
            )

    def center_point(self):
        return Point((self.__x1 + self.__x2) / 2, (self.__y1 + self.__y2) / 2)

    def draw_move(self, other, undo=False):
        self.__window.draw_line(
            Line(self.center_point(), other.center_point()),
            UNDO_COLOR if undo else PATH_COLOR,
        )
