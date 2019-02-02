import copy

from PIL import Image
import numpy as np
from functools import reduce
import random

# im = Image.open("C:/Users/juicy/OneDrive/Desktop/Photos/maze1.png")


# order is pixels[x, y] (not row, col)

# print(list(im.getdata()))

class Maze:
    DIRECTIONS = list(map(np.array, [[1, 0], [0, -1], [-1, 0], [0, 1]]))
    BLACK = (0, 0, 0)
    WHITE = (150, 150, 150)

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = Image.new('RGB', (width, height), self.BLACK)
        self.pos = np.array([0, 0])
        self.path = [np.copy(self.pos)]
        self.data = [[(0, 0, 0)] * width for i in range(height)]  # color data represented in row/col format
        self.set_cell(self.pos, self.WHITE)
        self.pixels = self.image.load()  # not sure if needed

    def update_image(self):
        image_data = list(reduce((lambda x, y: x + y), self.data))
        self.image.putdata(image_data)

    def generate_maze(self):
        while self.path:
            while True:
                valid_directions = list(filter(self.valid_dir, self.DIRECTIONS))
                if not valid_directions:
                    break
                self.pos += random.choice(valid_directions)
                self.path.append(np.copy(self.pos))
                self.set_cell(self.pos, self.WHITE)


    def has_move(self):
        return any(map(self.valid_dir, self.DIRECTIONS))

    def valid_dir(self, direction):
        new_pos = self.pos + direction
        filtered_neighbors = list(filter(lambda pos: self.get_cell(pos) == self.WHITE, self.neighbors(new_pos)))
        return (self.valid_pos(new_pos)
                and self.get_cell(new_pos) == self.BLACK
                and np.array_equal(filtered_neighbors, [self.pos]))

    def valid_pos(self, pos):
        return 0 <= pos[0] < self.width and 0 <= pos[1] < self.height

    def neighbors(self, pos):
        """Returns the positions of the neighbor cells of pos."""
        neighbor_positions = map(lambda direction: pos + direction, self.DIRECTIONS)
        return list(filter(self.valid_pos, neighbor_positions))

    def get_cell(self, pixel_pos):
        return self.data[pixel_pos[1]][pixel_pos[0]]

    def set_cell(self, pixel_pos, new_data):
        pixel_pos = np.copy(pixel_pos)
        self.data[pixel_pos[1]][pixel_pos[0]] = new_data
        #  self.data[pixel_pos[1]][pixel_pos[0]] = new_data


maze1 = Maze(50, 50)
#  neighbors = maze1.neighbors((0, 0))
#  print(maze1.pos)
maze1.generate_maze()
maze1.update_image()

print(maze1.path)

#  print(list(reduce((lambda x, y: x + y), maze1.data)))
#  maze1.image.show()
out = maze1.image.resize((500, 500))
out.show()
#  print(maze1.data)
#  print(maze1.data[2][4])
