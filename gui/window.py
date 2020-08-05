import time
import glob
from tkinter import *
from tkinter import ttk
from maze import Maze
from dijkstras import DJ
from DepthFirst import DFS
from PIL import Image, ImageTk

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

        # make Go command
        def goCom():

            maze_selection = self.file_Sel.get()
            im = Image.open("./examples/" + maze_selection + ".png")
            maze = Maze(im)

            #depth first search on the file
            if self.alg_Sel.get() == "DFS":
                #solve and time execution
                dfs = DFS(maze)
                t0 = time.time()
                dfs.solve()
                t1 = time.time()

                #set the view image
                dfs.write_img()
                img = dfs.maze.im.resize((500, 500), Image.NEAREST)
                img = ImageTk.PhotoImage(img)
                panel = Label(self.view_frame, image = img)
                panel.photo = img
                panel.place(relwidth = 1, relheight = 1)

                #update the results information
                self.checked_txt.set("Nodes Checked: {}".format(len(dfs.visited)))
                self.path_txt.set("Path Length: {}".format(len(dfs.answer)))
                self.timed_txt.set("Time Elapsed: {} ms".format((t1 - t0) * 1000))


            elif self.alg_Sel.get() == "Dijkstra's":
                #solve and time execution
                dj = DJ(maze)
                t0 = time.time()
                dj.solve()
                t1 = time.time()

                #set the view image
                dj.write_img()
                img = dj.maze.im.resize((500, 500), Image.NEAREST)
                img = ImageTk.PhotoImage(img)
                panel = Label(self.view_frame, image = img)
                panel.photo = img
                panel.place(relwidth = 1, relheight = 1)

                #update the results information
                self.checked_txt.set("Nodes Checked: {}".format(len(dj.visited)))
                self.path_txt.set("Path Length: {}".format(len(dj.answer)))
                self.timed_txt.set("Time Elapsed: {} ms".format((t1 - t0) * 1000))

	# make go button
        self.goBtn = Button(self.action_frame, text="GO", command = goCom)
        self.goBtn.place(relwidth = .33, relheight=.25, relx = 2/3, rely=1/4)

	# create dropdown selection for algorithms
        self.alg_Sel = ttk.Combobox(self.action_frame, values=["--Select an Algorithm--", "Dijkstra's", "DFS"])
        self.alg_Sel.current(0)
        self.alg_Sel.place(relwidth = .33, relheight=.25, relx = 1/3, rely=1/4)

        # create dropdown for file selection
        files = ["--Select a Maze--", "10x10", "20x20", "30x30", "40x40", "50x50", "60x60", "70x70", "80x80", "90x90", "100x100"]
        self.file_Sel = ttk.Combobox(self.action_frame, values=files)
        self.file_Sel.current(0)
        self.file_Sel.place(relwidth = .33, relheight=.25, relx = 0, rely = 1/4)

	# results labels and the strings to fill them with
        self.checked_txt = StringVar()
        self.path_txt = StringVar()
        self.timed_txt = StringVar()

        #now the labels will be updated when the stringvariables are updated
        checked = Label(self.results_frame, textvariable=self.checked_txt, bg = "#123456", fg = "#FFFFFF")
        path = Label(self.results_frame, textvariable=self.path_txt, bg = "#123456", fg = "#FFFFFF")
        timed = Label(self.results_frame, textvariable=self.timed_txt, bg = "#123456", fg = "#FFFFFF")

        #pack the labels onto the results frame
        checked.pack()
        path.pack()
        timed.pack()

    def init_frames(self, screen_width, screen_height):

        # declare the frames as slaves to the root window
        self.view_frame = Frame(
            self.root, bg="#FFFFFF", bd=5, relief="ridge")
        self.results_frame = Frame(
            self.root, bg="#123456", bd=0, relief="ridge")
        self.action_frame = Frame(
            self.root, bg="#123456", bd=0, relief="ridge")

        # place the frames onto a relative grid on the master window
        self.view_frame.grid(row=0, column=0, sticky="nsew")
        self.results_frame.grid(row=0, column=1, rowspan=2, sticky="nsew")
        self.action_frame.grid(row=1, column=0, sticky="nsew")

        # add weights to the columns
        self.root.grid_columnconfigure(0, weight=3)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=3)
        self.root.grid_rowconfigure(1, weight=1)
