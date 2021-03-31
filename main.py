from tkinter import *
import tkinter as tk
from board import Board
import tools

BTNWIDTH = 20 
ROOTWIDTH = 1020
ROOTHEIGHT = 700

# Creating the root window
root = tk.Tk()
root.minsize(ROOTWIDTH, ROOTHEIGHT)
root.title("Jeu de la vie")
root.configure(bg=Board.BG)
root.resizable(False, False)

fBoard  = Frame(root, bg=Board.BG)
fOption = Frame(root, bg=Board.BG)

fBoard.grid(row=0, column=0, sticky="ns")
fOption.grid(row=0, column=1, sticky="NESW", padx=(20, 10), pady=(10,0))

b = Board(fBoard)
b.drawBoard()

btnZoomIn = Button(fOption, text="Zoom in!", width=BTNWIDTH, command = lambda: tools.zoomIn(b))
btnZoomIn.grid(sticky="n", pady=(10,0))

btnZoomOut = Button(fOption, text="Zoom out!", width=BTNWIDTH, command = lambda: tools.zoomOut(b))
btnZoomOut.grid(sticky="n", pady=(10,0))
    
btnEvolve = Button(fOption, text="Evolve", width=BTNWIDTH)
btnEvolve.grid(sticky="n", pady=(10,0))

fOption.grid_columnconfigure(0, weight=1)
fOption.grid_columnconfigure(0, weight=1)

root.rowconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Launching
root.mainloop()