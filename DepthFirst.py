"""
Below is the implementation of using
Depth First search to solve the mazes
"""
from maze import Maze
from ext import Stack


def DFS(maze):

    # create a new path object which will hold integer values
    # representing the nodes in the path from start to finish
    path = Maze.Path()

    start_node = 1
    end_node = maze.num_nodes

    # TODO
