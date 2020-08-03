"""
Below is the implementation of using
Depth First search to solve the mazes
"""
from PIL import Image
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
    # this needs to be called over and over again until it returns true
    # use with make_gif method to create animation of maze being solved
    def advance(self):

        if not self.stack.empty():

            self.current_node = self.stack.peek()
            self.stack.pop()

            if not self.current_node in self.visited:
                
                self.visited.add(self.current_node)
                self.answer.append(self.current_node)

                self.stack.push(self.current_node)

                if self.current_node == self.end_node:
                    return True

                for i in self.graph[self.current_node]:
                    if not i in self.visited:
                        self.stack.push(i)

            else:
                if self.current_node in self.answer:
                    self.answer.pop()

            return False


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
                if curr in self.answer:
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

    # this method is used to create a gif instead of a png
    def make_gif(self, filepath):

        # list to hold intermediate images
        images = []
        
        while not self.advance():
            
            # copy of the image object
            copy = self.maze.im.copy()

            #convert to rgb
            copy = copy.convert("RGB")
            px = copy.load()

            for node in self.answer:

                location = self.positions[node]
                px[location] = (255, 0 ,0)

            images.append(copy)

        # do this one more time for the solved frame
        copy = self.maze.im.copy()

        #convert to rgb
        copy = copy.convert("RGB")
        px = copy.load()

        for node in self.answer:

            location = self.positions[node]
            px[location] = (255, 0 ,0)

        images.append(copy)
        
        # resize the images to make them easier to view
        # since gifs are difficult to resize after creation
        for i in range(len(images)):
            images[i] = images[i].resize((500,500), Image.NEAREST)

        images[0].save(filepath, format="GIF",
                append_images=images[1:],
                save_all=True,
                duration=300, Loop=0, quality=100)
