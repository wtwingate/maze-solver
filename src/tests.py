import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 12
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(maze._cells), num_cols)
        self.assertEqual(len(maze._cells[0]), num_rows)

    def test_large_maze_create_cells(self):
        num_cols = 100
        num_rows = 100
        maze = Maze(100, 100, num_rows, num_cols, 100, 100)
        self.assertEqual(len(maze._cells), num_cols)
        self.assertEqual(len(maze._cells[0]), num_rows)

    def test_break_entrance_and_exit(self):
        maze = Maze(0, 0, 10, 10, 10, 10)
        maze._break_entrance_and_exit()
        self.assertEqual(maze._cells[0][0].north_wall, False)
        self.assertEqual(maze._cells[-1][-1].south_wall, False)


if __name__ == "__main__":
    unittest.main()
