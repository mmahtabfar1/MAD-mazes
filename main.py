from PIL import Image
from maze import Maze
from ext import Priority_Queue

# program execution starts here
if __name__ == "__main__":

    im = Image.open("mazes/tiny.png")
    maze = Maze(im)

    print("\nMaze printing below:")
    maze.print()

    print("\nAdjacency List printing below:")
    maze.print_graph()
