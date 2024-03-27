from graphics import Window
from cell import Cell


def main():
    window = Window(800, 600)

    cell1 = Cell(window, 200, 200, 300, 300)
    cell2 = Cell(window, 300, 200, 400, 300)
    cell1.draw()
    cell2.draw()
    cell1.draw_move(cell2)
    cell1.draw_move(cell2, True)

    window.wait_for_close()


main()
