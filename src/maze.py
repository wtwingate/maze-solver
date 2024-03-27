from cell import Cell
from time import sleep


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_cols):
            new_col = []
            for j in range(self._num_rows):
                cell_x1 = (i * self._cell_size_x) + self._x1
                cell_y1 = (j * self._cell_size_y) + self._y1
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

    def _animate(self):
        self._window.redraw()
        sleep(0.05)
