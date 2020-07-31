""" Dijkstra's Algorithm"""

from ext import Priority_Queue

class DJ:

    class Node(self, id, dist):
        self.id = id
        self.distance_from_origin = dist

    def __init__(self, maze):
        
        #instance variables for the maze
        self.maze = maze
        self.graph = maze.graph
        self.positions = maze.node_locations
        self.start_node = 0
        self.end_node = maze.num_nodes

        # instance variables for dijkstras
        self.visited = set()
        self.unvisited = set()
        self.distances = Priority_Queue()
        self.predecessors = [-1] * maze.num_nodes

        # add all of the nodes to the unvisited set
        # note: nodes are just numbers
        for i in range(1, maze.num_nodes + 1):
            self.unvisited.add(i)

        # the answer
        self.answer = deque()


    """
    solves the maze using dijkstras algorithm.
    the answer will be in the self.answer instance variable
    """
    def solve(self):

        # remove the start vertex from the unvisited
        # and add it to the visited set

        self.unvisited.remove(1)
        self.visited.add(1)

        # do this while unvisited set is not empty
        while len(self.unvisited) != 0:



            pass

        


        pass
        
