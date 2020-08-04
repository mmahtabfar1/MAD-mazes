
import sys
import time
import glob
import argparse
from PIL import Image
from maze import Maze
from dijkstras import DJ
from DepthFirst import DFS
from gui import main as gui_main

"""
Authors: Mahan Mahtabfar, Derek Musial, Amer Khalifa
"""
def main():

    #argument parser to parse command line arugments
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", type=str, help="the path to the file(s) to solve", default="")
    parser.add_argument("-g", "--gif", help="write out result as gif instead of png", action = "store_true")
    parser.add_argument("--dijkstras", help="solve using dijkstras algorithm", action = "store_true", default=False)
    parser.add_argument("--DFS", help="solve using DFS", action = "store_true", default=False)
    
    args = parser.parse_args()


    if args.path != "":

        #make sure that the path is correct attempt to complete if not
        if ".png" in args.path:
            files = glob.glob(args.path)

        elif args.path[-1] == "/":
            files = glob.glob(args.path + "*.png")

        else:
            files = glob.glob(args.path + "/*.png")

        if len(files) == 0:
            print("Error: could not understand the path given")
            sys.exit(1)

        if args.gif:

            if(args.dijkstras):
                print("Sorry creating a gif of dijkstras is not supported")
                sys.exit(1)

            print("will make a gif using DFS!")

            for path in files:
                print(":: Loading file \"{}\"".format(path))
                im = Image.open(path)

                print(":: Building maze:")
                maze = Maze(im)
                dfs = DFS(maze)

                print(":: Creating GIF using DFS")
                dfs.make_gif(path)

        #solve each file in files
        else:
            for path in files:
                print(":: Loading file \"{}\"".format(path))
                im = Image.open(path)
                print(":: Building maze:\n")
                maze = Maze(im)

                #add dijkstras solution
                if args.dijkstras:
                    dj = DJ(maze)

                    print(":: Solving using Dijkstra's Algorithm")
                    t0 = time.time()
                    dj.solve()
                    t1 = time.time()
                    print("\nRuntime for Dijkstra's Algirhtm: {} ms".format((t1 - t0)* 1000))
                    print("Nodes examined: {}".format(len(dj.visited)))
                    print("Path length: {}\n".format(len(dj.answer)))
                    dj.write_out(path)

                if args.DFS:
                    dfs = DFS(maze)

                    print(":: Solving using DFS")
                    t0 = time.time()
                    dfs.solve()
                    t1 = time.time()
                    print("\nRuntime for DFS: {} ms".format((t1 - t0) * 1000))
                    print("Nodes examined: {}".format(len(dfs.visited)))
                    print("Path length: {}\n".format(len(dfs.answer)))
                    dfs.write_out(path)
                
                if not args.dijkstras and not args.DFS:
                    print("Error: please specify either --dijkstras or --DFS")
                    sys.exit(1)
                
    else:
        print(":: Running in gui mode:")
        gui_main()
    
# program execution starts here
if __name__ == "__main__":
    main()

