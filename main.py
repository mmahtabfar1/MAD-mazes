from PIL import Image
from maze import Maze

# program execution starts here
if __name__ == "__main__":

    im = Image.open("mazes/tiny.png")
    maze = Maze(im)
    maze.print()
    print()
    maze.print_graph()
