from graphics import Window
from maze import Maze
from constants import WIN_WIDTH, WIN_HEIGHT, CELL_SIZE


def main():
    window = Window(WIN_WIDTH, WIN_HEIGHT)
    num_rows = int((WIN_HEIGHT / CELL_SIZE) - 2)
    num_cols = int((WIN_WIDTH / CELL_SIZE) - 2)

    maze = Maze(CELL_SIZE, CELL_SIZE, num_rows, num_cols, CELL_SIZE, CELL_SIZE, window)
    maze._break_walls_r(0, 0)
    maze.solve()

    window.wait_for_close()


main()
