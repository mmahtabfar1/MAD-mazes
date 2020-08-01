"""
Below is the implementation of using
Depth First search to solve the mazes
"""
from maze import Maze
from ext import Stack


class DFS:

    def __init__(self, maze):

        self.maze = maze
        self.positions = maze.node_locations
        self.graph = maze.graph

        self.answer = list()
        self.visited = set()
        self.stack = Stack()

        self.current_node = 1
        self.end_node = maze.num_nodes

        self.stack.push(1)

    # this method will advance the current node and stack using DFS
    # this needs to be called over and over again with time in-between for
    # use with the GUI should return true if the maze has been solved, false otherwise
    def advance(self):

        if not self.stack.empty():

            self.current_node = self.stack.peek()

        pass

    # this method will solve the maze all at once for use with CLI
    def solve(self):

        while not self.stack.empty():

            # get the top of the stack as the current value
            curr = self.stack.peek()
            self.stack.pop()
            # print("current node: {}".format(curr))

            # if we have already visited this node just remove the
            # last node from the answer path
            if not curr in self.visited:

                # add curr to be a visited node and add it to answer
                self.visited.add(curr)
                self.answer.append(curr)

                # add curr to the stack as well but under its children
                self.stack.push(curr)

                # if the top of the stack is the target value then we have
                # reached the solution
                if curr == self.end_node:
                    break

                # otherwise add all of the current node's unvisited children to the stack
                for i in self.graph[curr]:
                    if not i in self.visited:
                        self.stack.push(i)

            else:
                self.answer.pop()

    # this method will write out the solved maze to a new png file
    # with the DFS solution in red pixels
    def write_out(self, filepath):

        # first convert the image to rgb
        self.maze.im = self.maze.im.convert("RGB")
        px = self.maze.im.load()

        for node in self.answer:

            location = self.positions[node]
            px[location] = (255, 0, 0)

        self.maze.im.save(filepath)

    # this method is used to create a gif for the github page
    def make_gif(self, filepath):

        pass
