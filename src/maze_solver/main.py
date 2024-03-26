from graphics import Window, Point, Line


def main():
    window = Window(800, 600)
    point1 = Point(200, 500)
    point2 = Point(500, 200)
    line = Line(point1, point2)
    window.draw_line(line, "black")
    window.wait_for_close()


main()
