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
        self.start_node = 1
        self.end_node = maze.num_nodes

        # instance variables for dijkstras
        self.INFINITY = 2,147,483,647
        self.visited = set()
        self.unvisited = set()
        self.distances = Priority_Queue()
        self.predecessors = [-1] * maze.num_nodes

        # add the start node to the visited set
        self.visited.add(self.start_node)

        # add the remaining Nodes to the unvisited set
        # note: nodes are just numbers
        for i in range(2, maze.num_nodes + 1):
            self.unvisited.add(i)

        # add all of the nodes to the distances heap.
        # insert the start node with a distance 0 and all others with self.INFINITY
        # which is the maximum integer value in C
        self.distances.insert(1, 0)

        for i in range(2, self.maze.num_nodes + 1):
            self.distances.insert(self.INFINITY, i)
        


        # the answer deque representing the shortest path from start
        # node to the end node
        self.answer = deque()


    """
    solves the maze using dijkstras algorithm.
    the answer will be in the self.answer instance variable
    """
    def solve(self):

        # remove the start vertex from the unvisited
        # and add it to the visited set

        # do this while unvisited set is not empty
        while len(self.unvisited) != 0:

            cur = distances.extract_min()

            self.unvisited.remove(cur[0])
            self.visited.add(cur[0])

            neighbors = self.graph[cur[0]]

            for v in neighbors:
                if v in self.unvisited:
                    if cur[1]+1 < self.distances.get_distance[v]:
                        self.distances.decrease_key(v, cur[1]+1)
                        self.predecessors[v] = cur[0]

                      
        current = self.end_node
        while (self.predecessors[current] != self.start_node):
            current = self.predecessors[current]
            self.answer.appendleft(current)

        self.answer.appendleft(self.start_node)

        
