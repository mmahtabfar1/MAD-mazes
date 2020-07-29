from PIL import Image
from maze import Maze
from ext import Priority_Queue
from gui import main as gui_main
from DepthFirst import DFS

# program execution starts here
if __name__ == "__main__":

    im = Image.open("mazes/tiny.png")
    maze = Maze(im)

    print("\nMaze printing below:")
    maze.print()

    print("\nAdjacency List printing below:")
    maze.print_graph()

    dfs = DFS(maze)
    dfs.solve()

    print(dfs.answer)
