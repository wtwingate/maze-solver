from cell import Cell
from time import sleep
from constants import *
import random


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        window=None,
        seed=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        self._seed = random.seed(seed)
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for x in range(self._num_cols):
            new_col = []
            for y in range(self._num_rows):
                cell_x1 = (x * self._cell_size_x) + self._x1
                cell_y1 = (y * self._cell_size_y) + self._y1
                cell_x2 = cell_x1 + self._cell_size_x
                cell_y2 = cell_y1 + self._cell_size_y
                new_col.append(Cell(cell_x1, cell_y1, cell_x2, cell_y2, self._window))
            self._cells.append(new_col)
        self._draw_cells()

    def _draw_cells(self):
        if self._window is None:
            return
        for column in self._cells:
            for cell in column:
                cell.draw()
                self._animate()
        self._break_entrance_and_exit()

    def _draw_cell(self, cell):
        if self._window is None:
            return
        cell.draw()
        self._animate()

    def _animate(self):
        self._window.redraw()
        sleep(0.01)

    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        exit = self._cells[-1][-1]
        entrance.north_wall = False
        self._draw_cell(entrance)
        exit.south_wall = False
        self._draw_cell(exit)

    def _break_walls_r(self, x, y):
        current_cell = self._cells[x][y]
        current_cell.visited = True
        while True:
            to_visit = []
            for dir in NEIGHBOR_DIRS:
                next_x = x + dir[0]
                next_y = y + dir[1]
                if (
                    0 <= next_x < self._num_cols
                    and 0 <= next_y < self._num_rows
                    and self._cells[next_x][next_y].visited == False
                ):
                    to_visit.append((next_x, next_y))
            if len(to_visit) == 0:
                self._draw_cell(current_cell)
                return
            next_cell = to_visit[random.randrange(len(to_visit))]
            self._break_wall(x, y, next_cell[0], next_cell[1])
            self._break_walls_r(next_cell[0], next_cell[1])

    def _break_wall(self, x1, y1, x2, y2):
        current_cell = self._cells[x1][y1]
        next_cell = self._cells[x2][y2]
        if x1 == x2 and y1 < y2:
            current_cell.south_wall = False
            next_cell.north_wall = False
        elif x1 == x2 and y1 > y2:
            current_cell.north_wall = False
            next_cell.south_wall = False
        elif x1 < x2 and y1 == y2:
            current_cell.east_wall = False
            next_cell.west_wall = False
        elif x1 > x2 and y1 == y2:
            current_cell.west_wall = False
            next_cell.east_wall = False
        else:
            raise Exception("Error: invalid cell coordinates")
        self._draw_cell(current_cell)
        self._draw_cell(next_cell)
