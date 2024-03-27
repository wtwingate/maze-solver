from graphics import Window
from maze import Maze


def main():
    width = 800
    height = 600
    cell_size = 40
    window = Window(width, height)
    num_rows = int((height / cell_size) - 2)
    num_cols = int((width / cell_size) - 2)

    maze = Maze(
        cell_size,
        cell_size,
        num_rows,
        num_cols,
        cell_size,
        cell_size,
        window,
        seed=None,
    )
    maze.solve()
    window.wait_for_close()


main()
