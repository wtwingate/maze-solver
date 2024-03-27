from tkinter import Tk, BOTH, Canvas

WALL_COLOR = "black"
PATH_COLOR = "red"


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack()
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.__p1 = p1
        self.__p2 = p2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.__p1.x, self.__p1.y, self.__p2.x, self.__p2.y, fill=fill_color, width=2
        )
        canvas.pack()


class Cell:
    def __init__(self, window, x1, y1, x2, y2):
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
