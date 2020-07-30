""" Dijkstra's Algorithm"""

from ext import Priority_Queue

class DJ:
	def __init__(self, maze):
		self.maze = maze
        self.positions = maze.node_locations
        self.graph = maze.graph


	def solve(self):
		"""some more code"""

	def write_out(self):
		# first convert the image to rgb
        self.maze.im = self.maze.im.convert("RGB")
        px = self.maze.im.load()

        for node in self.answer:

            location = self.positions[node]
            px[location] = (255, 0, 0)

        self.maze.im.save(filepath)
