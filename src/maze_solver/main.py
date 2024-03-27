from graphics import Window, Point, Line, Cell


def main():
    window = Window(800, 600)

    cell1 = Cell(window, 200, 200, 300, 300)
    cell2 = Cell(window, 300, 300, 400, 400)
    cell1.north_wall = False
    cell1.south_wall = False
    cell2.east_wall = False
    cell2.west_wall = False
    cell1.draw()
    cell2.draw()

    window.wait_for_close()


main()
