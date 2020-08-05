""" Dijkstra's Algorithm"""
from ext import Priority_Queue
from collections import deque

class DJ:

    def __init__(self, maze):
        
        #instance variables for the maze
        self.maze = maze
        self.graph = maze.graph
        self.positions = maze.node_locations
        self.start_node = 1
        self.end_node = maze.num_nodes

        # instance variables for dijkstras
        self.INFINITY = 2147483647
        self.visited = set()
        self.distances = Priority_Queue()
        self.predecessors = [-1] * (maze.num_nodes+1)

        # add all of the nodes to the distances heap.
        # insert the start node with a distance 0 and all others with self.INFINITY
        # which is the maximum integer value in C
        self.distances.insert(1, 0)

        for i in range(2, self.maze.num_nodes + 1):
            self.distances.insert(i, self.INFINITY)

        # the answer deque representing the shortest path from start
        # node to the end node
        self.answer = deque()

    """
    solves the maze using dijkstras algorithm.
    the answer will be in the self.answer instance variable
    """
    def solve(self):

        while not self.distances.empty():
        
            if self.end_node in self.visited:
                break

            curr = self.distances.extract_min()
            
            self.visited.add(curr[0])

            neighbors = self.graph[curr[0]]

            for v in neighbors:
            
                if not v in self.visited:
                
                    if curr[1] + 1 < self.distances.get_distance(v):
                        self.distances.decrease_key(v, curr[1] + 1)
                        self.predecessors[v] = curr[0]

        current = self.end_node
        self.answer.appendleft(self.end_node)

        while (self.predecessors[current] != self.start_node):
            if(self.predecessors[current] == -1):
                break
            current = self.predecessors[current]
            self.answer.appendleft(current)

        self.answer.appendleft(self.start_node)

    def write_img(self):

        # first convert the image to rgb
        self.maze.im = self.maze.im.convert("RGB")
        px = self.maze.im.load()

        for node in self.answer:

            location = self.positions[node]
            px[location] = (0, 0, 255)

    def write_out(self, filepath):

        # first convert the image to rgb
        self.maze.im = self.maze.im.convert("RGB")
        px = self.maze.im.load()

        for node in self.answer:

            location = self.positions[node]
            px[location] = (0, 0, 255)

        self.maze.im.save(filepath)

