from tkinter import *
from tkinter import ttk
from gui.window import Window


def main():
    root = Tk()
    root.title("MAD-mazes")
    window = Window(root)
    root.mainloop()

if __name__ == "__main__":
    main()
