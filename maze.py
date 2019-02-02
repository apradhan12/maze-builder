# hello
# pls help

import wx


class Maze:
    """Represents a 2D square maze."""

    def __init__(self, side_len):
        """Initialize the maze to an empty grid of size sideLength by sideLength."""
        self.side_len = side_len
        self.contents = [['M'] * side_len] * side_len

    def __str__(self):
        """Returns the contents of the maze as a string, where ' ' represents a blank
           space, 'M' represents a wall, '!' represents the start, and '*' represents
           the finish."""
        return '\n'.join([''.join(self.contents[i]) for i in range(self.side_len)])


maze1 = Maze(5)
print(maze1)
print("banana")
