from PIL import Image
from maze import Maze


#takes the image object and prints it to stdout
#in a readable way (only works for small images)

def print_maze(im):

    data = list(im.getdata(0))

    #the width and height of the image in pixels
    width, height = im.size

    print("Total Pixels: ",len(data))
    print("Height: ",height)
    print("Width: ",width)
    
    i = 0
    while i < len(data) - width:
        print(data[i:i+width])
        i += width

    """
    this will print out a python list that should look like the maze 
    the 1's will represent a valid open spot and 0's represent the black tiles
    which are walls in the png image
    """


#program execution starts here
if __name__ == "__main__":

    im = Image.open("mazes/tiny.png")
    print_maze(im)



