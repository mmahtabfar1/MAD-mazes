from PIL import Image
from maze import Maze
from ext import Priority_Queue
#from gui import main as gui_main
from DepthFirst import DFS
from dijkstras import DJ

"""
Authors: Mahan Mahtabfar, Derek Musial, Amer Khalifa
"""

# program execution starts here
if __name__ == "__main__":

    im = Image.open("mazes/test2.png")
    maze = Maze(im)

    #print("\nMaze printing below:")
    #maze.print()

    #print("\nAdjacency List printing below:")
    #maze.print_graph()

    dfs = DFS(maze)
    dfs.solve()

    print(dfs.answer)
    dfs.write_out("mazes/test2_solved_dfs.png")

    #gui_main()

    im2 = Image.open("mazes/test2.png")
    maze = Maze(im2)

    dj = DJ(maze)
    dj.solve()
    print(dj.answer)
    dj.write_out("mazes/test2_solved_dj.png")
