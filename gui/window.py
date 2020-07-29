from tkinter import *
from maze import Maze


class Window:

    def __init__(self, root):

        self.root = root

        # trick to get the screen size
        self.root.attributes("-fullscreen", True)
        self.root.state("iconic")
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.attributes("-fullscreen", False)
        self.root.deiconify()

        self.root.title("MAD-mazes")

        # set window geometry
        self.root.geometry(f"{self.screen_width}x{self.screen_height}")
        self.root.minsize(width=self.screen_width//2,
                          height=self.screen_height//2)
        self.root.maxsize(width=self.screen_width, height=self.screen_height)

        # create the frames for the window
        self.init_frames(self.screen_width, self.screen_height)

    def init_frames(self, screen_width, screen_height):

        # declare the frames as slaves to the root window
        self.view_frame = Frame(
            self.root, bg="#808080", bd=5, relief="ridge")
        self.results_frame = Frame(
            self.root, bg="#808080", bd=5, relief="ridge")
        self.action_frame = Frame(
            self.root, bg="#808080", bd=5, relief="ridge")

        # place the frames onto a relative grid on the master window
        self.view_frame.grid(row=0, column=0, sticky="nsew")
        self.results_frame.grid(row=1, column=2, rowspan=2, sticky="nsew")
        self.action_frame.grid(row=1, column=0, sticky="nsew")

        # add weights to the columns
        self.root.grid_columnconfigure(0, weight=3)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=3)
        self.root.grid_rowconfigure(1, weight=1)
