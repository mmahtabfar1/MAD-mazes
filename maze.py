class Maze:

    class Path:

        def __init__(self):
            # a list of integers representing the nodes in order
            path = list()

    # creates the maze given an a pillow image object
    def __init__(self, im):

        # adjacency list in the form of a python dictionary
        # same as std::map in c++
        self.graph = {}

        # another dictionary to map node ID's to their
        # pixel position in the image
        self.node_locations = {}

        # information on the maze
        self.num_nodes = 0
        self.WIDTH, self.HEIGHT = im.size
        self.raw_data = list()

        # parse the image data list into a 2-d list for simplicity
        for i in range(0, len(list(im.getdata(0))), self.WIDTH):
            self.raw_data.append(list(im.getdata(0))[i: i + self.WIDTH])

        # give each node in the raw_data list a unique number
        # these are given in the order they are encountered
        # scanning from the top down one row at a time
        # also add the nodes position to the position dictionary
        counter = 1
        for i in range(len(self.raw_data)):

            for j in range(self.WIDTH):

                if self.raw_data[i][j] != 0:

                    self.raw_data[i][j] = counter

                    # add location info and add node to adjlist
                    self.node_locations[counter] = (i, j)
                    self.graph[counter] = []

                    # increment counter and number of nodes by 1
                    self.num_nodes += 1
                    counter += 1

        # process the maze, adding nodes to the adjacency
        # along with their edges and weights

        # process the top row on its own to avoid indexing errors
        for i in range(self.WIDTH):

            # reached the entry node so add its edge to the adjlist
            if self.raw_data[0][i] != 0:
                self.graph[self.raw_data[0][i]] = [self.raw_data[1][i]]

        # process the middle rows of the image
        # TODO
        for i in range(1, self.HEIGHT - 1):

            for j in range(1, self.WIDTH - 1):

                curr = self.raw_data[i][j]

                # if the current pixel is a node
                if curr != 0:

                    # the pixel above
                    above = self.raw_data[i - 1][j]

                    # the pixel to the right
                    right = self.raw_data[i][j + 1]

                    # the pixel to the left
                    left = self.raw_data[i][j - 1]

                    below = self.raw_data[i + 1][j]

                    # if the pixel above is a node
                    if above != 0:
                        self.graph[curr].append(above)

                    # check the node to its right
                    if right != 0:
                        self.graph[curr].append(right)

                    # check the node to its left
                    if left != 0:
                        self.graph[curr].append(left)

                    # check the node below
                    if below != 0:
                        self.graph[curr].append(below)

        # process the bottom row on its own
        for i in range(self.WIDTH):

            curr = self.raw_data[self.HEIGHT - 1][i]

            # reached the exit node so add its edge to the adjlist
            if curr != 0:
                self.graph[curr].append(self.raw_data[self.HEIGHT - 2][i])

    # print out the adjacency list representing the graph
    # only useful for small graphs for debugging purposes
    def print_graph(self):
        for key in self.graph:
            print("{}: {}".format(key, self.graph[key]))

    # print the maze one row at a time
    # 0's are walls corresopnding to black pixels in the image
    # any nonzero number is a node. represents a white pixel in the image
    def print(self):
        for i in self.raw_data:
            print(i)
