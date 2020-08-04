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

            # for 10x10 Maze
            if file_Sel.get() == "10x10":
                im = Image.open("./examples/10x10_69.png")
                maze = Maze(im)
                if alg_Sel.get() == "DFS":
                    # solve DFS for given input
                    dfs = DFS(maze)
                    t0 = time.time()
                    dfs.solve()
                    t1 = time.time()
                    dfs.write_out("./examples/10x10_DFS.png")
                    # print image of solved maze
                    img = Image.open("./examples/10x10_DFS.png").resize((500, 500), Image.NEAREST)
                    img = ImageTk.PhotoImage(img)
                    panel = Label(self.view_frame, image = img)
                    panel.photo = img
                    panel.place(relwidth = 1, relheight=1)
                    # print important info on the side
                    checked_txt = "Nodes Checked: " + str(len(dfs.visited))
                    path_txt = "Path Length: " + str(len(dfs.answer))
                    timed_txt = "Time Elapsed: " + str((t1 - t0) * 1000)
                    checked = Label(self.results_frame, text=checked_txt, bg = "#123456", fg = "#FFFFFF")
                    path = Label(self.results_frame, text=path_txt, bg = "#123456", fg = "#FFFFFF")
                    timed = Label(self.results_frame, text=timed_txt, bg = "#123456", fg = "#FFFFFF")
                    checked.pack()
                    path.pack()
                    timed.pack()
                    pass
                if alg_Sel.get() == "Dijkstra's":
                    dj = DJ(maze)
                    dj.solve()
                    dj.write_out("./examples/10x10_DJ.png")
                    img = Image.open("./examples/10x10_DJ.png").resize((500, 500), Image.NEAREST)
                    img = ImageTk.PhotoImage(img)
                    panel = Label(self.view_frame, image = img)
                    panel.photo = img
                    panel.place(relwidth = 1, relheight=1)
                    pass

            # for 20x20 Maze
            if file_Sel.get() == "20x20":
                im = Image.open("./examples/20x20_1.png")
                maze = Maze(im)
                if alg_Sel.get() == "DFS":
                    dfs = DFS(maze)
                    dfs.solve()
                    dfs.write_out("./examples/20x20_DFS.png")
                    img = Image.open("./examples/20x20_DFS.png").resize((500, 500), Image.NEAREST)
                    img = ImageTk.PhotoImage(img)
                    panel = Label(self.view_frame, image = img)
                    panel.photo = img
                    panel.place(relwidth = 1, relheight=1)
                    pass
                if alg_Sel.get() == "Dijkstra's":
                    dj = DJ(maze)
                    dj.solve()
                    dj.write_out("./examples/20x20_DJ.png")
                    img = Image.open("./examples/20x20_DJ.png").resize((500, 500), Image.NEAREST)
                    img = ImageTk.PhotoImage(img)
                    panel = Label(self.view_frame, image = img)
                    panel.photo = img
                    panel.place(relwidth = 1, relheight=1)
                    pass

            # for 30x30 Maze
            if file_Sel.get() == "30x30":
                im = Image.open("./examples/30x30_1.png")
                maze = Maze(im)
                if alg_Sel.get() == "DFS":
                    dfs = DFS(maze)
                    dfs.solve()
                    dfs.write_out("./examples/30x30_DFS.png")
                    img = Image.open("./examples/30x30_DFS.png").resize((500, 500), Image.NEAREST)
                    img = ImageTk.PhotoImage(img)
                    panel = Label(self.view_frame, image = img)
                    panel.photo = img
                    panel.place(relwidth = 1, relheight=1)
                    pass
                if alg_Sel.get() == "Dijkstra's":
                    dj = DJ(maze)
                    dj.solve()
                    dj.write_out("./examples/30x30_DJ.png")
                    img = Image.open("./examples/30x30_DJ.png").resize((500, 500), Image.NEAREST)
                    img = ImageTk.PhotoImage(img)
                    panel = Label(self.view_frame, image = img)
                    panel.photo = img
                    panel.place(relwidth = 1, relheight=1)
                    pass

            # for 40x40 Maze
            if file_Sel.get() == "40x40":
                im = Image.open("./examples/40x40_1.png")
                maze = Maze(im)
                if alg_Sel.get() == "DFS":
                    dfs = DFS(maze)
                    dfs.solve()
                    dfs.write_out("./examples/40x40_DFS.png")
                    img = Image.open("./examples/40x40_DFS.png").resize((500, 500), Image.NEAREST)
                    img = ImageTk.PhotoImage(img)
                    panel = Label(self.view_frame, image = img)
                    panel.photo = img
                    panel.place(relwidth = 1, relheight=1)
                    pass
                if alg_Sel.get() == "Dijkstra's":
                    dj = DJ(maze)
                    dj.solve()
                    dj.write_out("./examples/40x40_DJ.png")
                    img = Image.open("./examples/40x40_DJ.png").resize((500, 500), Image.NEAREST)
                    img = ImageTk.PhotoImage(img)
                    panel = Label(self.view_frame, image = img)
                    panel.photo = img
                    panel.place(relwidth = 1, relheight=1)
                    pass

            # for 50x50 Maze
            if file_Sel.get() == "50x50":
                im = Image.open("./examples/50x50_1.png")
                maze = Maze(im)
                if alg_Sel.get() == "DFS":
                    dfs = DFS(maze)
                    dfs.solve()
                    dfs.write_out("./examples/50x50_DFS.png")
                    img = Image.open("./examples/50x50_DFS.png").resize((500, 500), Image.NEAREST)
                    img = ImageTk.PhotoImage(img)
                    panel = Label(self.view_frame, image = img)
                    panel.photo = img
                    panel.place(relwidth = 1, relheight=1)
                    pass
                if alg_Sel.get() == "Dijkstra's":
                    dj = DJ(maze)
                    dj.solve()
                    dj.write_out("./examples/50x50_DJ.png")
                    img = Image.open("./examples/50x50_DJ.png").resize((500, 500), Image.NEAREST)
                    img = ImageTk.PhotoImage(img)
                    panel = Label(self.view_frame, image = img)
                    panel.photo = img
                    panel.place(relwidth = 1, relheight=1)
                    pass

            # for 60x60 Maze
            if file_Sel.get() == "60x60":
                im = Image.open("./examples/60x60_1.png")
                maze = Maze(im)
                if alg_Sel.get() == "DFS":
                    dfs = DFS(maze)
                    dfs.solve()
                    dfs.write_out("./examples/60x60_DFS.png")
                    img = Image.open("./examples/60x60_DFS.png").resize((500, 500), Image.NEAREST)
                    img = ImageTk.PhotoImage(img)
                    panel = Label(self.view_frame, image = img)
                    panel.photo = img
                    panel.place(relwidth = 1, relheight=1)
                    pass
                if alg_Sel.get() == "Dijkstra's":
                    dj = DJ(maze)
                    dj.solve()
                    dj.write_out("./examples/60x60_DJ.png")
                    img = Image.open("./examples/60x60_DJ.png").resize((500, 500), Image.NEAREST)
                    img = ImageTk.PhotoImage(img)
                    panel = Label(self.view_frame, image = img)
                    panel.photo = img
                    panel.place(relwidth = 1, relheight=1)
                    pass

            # for 70x70 Maze
            if file_Sel.get() == "70x70":
                im = Image.open("./examples/70x70_1.png")
                maze = Maze(im)
                if alg_Sel.get() == "DFS":
                    dfs = DFS(maze)
                    dfs.solve()
                    dfs.write_out("./examples/70x70_DFS.png")
                    img = Image.open("./examples/70x70_DFS.png").resize((500, 500), Image.NEAREST)
                    img = ImageTk.PhotoImage(img)
                    panel = Label(self.view_frame, image = img)
                    panel.photo = img
                    panel.place(relwidth = 1, relheight=1)
                    pass
                if alg_Sel.get() == "Dijkstra's":
                    dj = DJ(maze)
                    dj.solve()
                    dj.write_out("./examples/70x70_DJ.png")
                    img = Image.open("./examples/70x70_DJ.png").resize((500, 500), Image.NEAREST)
                    img = ImageTk.PhotoImage(img)
                    panel = Label(self.view_frame, image = img)
                    panel.photo = img
                    panel.place(relwidth = 1, relheight=1)
                    pass

            # for 80x80 Maze
            if file_Sel.get() == "80x80":
                im = Image.open("./examples/80x80_1.png")
                maze = Maze(im)
                if alg_Sel.get() == "DFS":
                    dfs = DFS(maze)
                    dfs.solve()
                    dfs.write_out("./examples/80x80_DFS.png")
                    img = Image.open("./examples/80x80_DFS.png").resize((500, 500), Image.NEAREST)
                    img = ImageTk.PhotoImage(img)
                    panel = Label(self.view_frame, image = img)
                    panel.photo = img
                    panel.place(relwidth = 1, relheight=1)
                    pass
                if alg_Sel.get() == "Dijkstra's":
                    dj = DJ(maze)
                    dj.solve()
                    dj.write_out("./examples/80x80_DJ.png")
                    img = Image.open("./examples/80x80_DJ.png").resize((500, 500), Image.NEAREST)
                    img = ImageTk.PhotoImage(img)
                    panel = Label(self.view_frame, image = img)
                    panel.photo = img
                    panel.place(relwidth = 1, relheight=1)
                    pass

            # for 90x90 Maze
            if file_Sel.get() == "90x90":
                im = Image.open("./examples/90x90_1.png")
                maze = Maze(im)
                if alg_Sel.get() == "DFS":
                    dfs = DFS(maze)
                    dfs.solve()
                    dfs.write_out("./examples/90x90_DFS.png")
                    img = Image.open("./examples/90x90_DFS.png").resize((500, 500), Image.NEAREST)
                    img = ImageTk.PhotoImage(img)
                    panel = Label(self.view_frame, image = img)
                    panel.photo = img
                    panel.place(relwidth = 1, relheight=1)
                    pass
                if alg_Sel.get() == "Dijkstra's":
                    dj = DJ(maze)
                    dj.solve()
                    dj.write_out("./examples/90x90_DJ.png")
                    img = Image.open("./examples/90x90_DJ.png").resize((500, 500), Image.NEAREST)
                    img = ImageTk.PhotoImage(img)
                    panel = Label(self.view_frame, image = img)
                    panel.photo = img
                    panel.place(relwidth = 1, relheight=1)
                    pass

            # for 100x100 Maze
            if file_Sel.get() == "100x100":
                im = Image.open("./examples/100x100_1.png")
                maze = Maze(im)
                if alg_Sel.get() == "DFS":
                    dfs = DFS(maze)
                    dfs.solve()
                    dfs.write_out("./examples/100x100_DFS.png")
                    img = Image.open("./examples/100x100_DFS.png").resize((500, 500), Image.NEAREST)
                    img = ImageTk.PhotoImage(img)
                    panel = Label(self.view_frame, image = img)
                    panel.photo = img
                    panel.place(relwidth = 1, relheight=1)
                    pass
                if alg_Sel.get() == "Dijkstra's":
                    dj = DJ(maze)
                    dj.solve()
                    dj.write_out("./examples/100x100_DJ.png")
                    img = Image.open("./examples/100x100_DJ.png").resize((500, 500), Image.NEAREST)
                    img = ImageTk.PhotoImage(img)
                    panel = Label(self.view_frame, image = img)
                    panel.photo = img
                    panel.place(relwidth = 1, relheight=1)
                    pass

		# make go button
        goBtn = Button(self.action_frame, text="GO", command = goCom)
        goBtn.place(relwidth = .33, relheight=.25, relx = 2/3, rely=1/4)

	    # create dropdown selection for algorithms
        alg_Sel = ttk.Combobox(self.action_frame, values=["--Select an Algorithm--", "Dijkstra's", "DFS"])
        alg_Sel.current(0)
        alg_Sel.place(relwidth = .33, relheight=.25, relx = 1/3, rely=1/4)

		# create dropdown for file selection
        files = ["--Select a Maze--", "10x10", "20x20", "30x30", "40x40", "50x50", "60x60", "70x70", "80x80", "90x90", "100x100"]
        file_Sel = ttk.Combobox(self.action_frame, values=files)
        file_Sel.current(0)
        file_Sel.place(relwidth = .33, relheight=.25, relx = 0, rely = 1/4)

		# results labels
        result_txt = ""
        result1 = Label(self.results_frame, text="Glizzy Guzzler", bg = "#123456", fg = "#FFFFFF")
        result1.pack()

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
