from graphics import Window
from cell import Cell
from time import sleep


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__window = window
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        for i in range(self.__num_cols):
            new_col = []
            for j in range(self.__num_rows):
                cell_x1 = (i * self.__cell_size_x) + self.__x1
                cell_y1 = (j * self.__cell_size_y) + self.__y1
                cell_x2 = cell_x1 + self.__cell_size_x
                cell_y2 = cell_y1 + self.__cell_size_y
                new_col.append(Cell(self.__window, cell_x1, cell_y1, cell_x2, cell_y2))
            self.__cells.append(new_col)
        self.__draw_cells()

    def __draw_cells(self):
        for column in self.__cells:
            for cell in column:
                cell.draw()
                self.__animate()

    def __animate(self):
        self.__window.redraw()
        sleep(0.05)
