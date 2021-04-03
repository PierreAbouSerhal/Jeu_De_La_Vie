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

# fboard: Frame that contains the game board / fOption: Frame that contains the buttons + label
fBoard  = Frame(root, bg=Board.BG)
fOption = Frame(root, bg=Board.BG)

# Grid layout for both frames
fBoard.grid(row=0, column=0, sticky="ns")
fOption.grid(row=0, column=1, sticky="NESW", padx=(20, 10), pady=(10,0))

b = Board(fBoard)
b.drawBoard()

# Button zoom in: to zoom in the grid
btnZoomIn = Button(fOption, text = "Zoom in!", width = BTNWIDTH, command = lambda: tools.zoomIn(b))
btnZoomIn.grid(sticky = "n", pady = (10,0))

# Button zoom out: to zoom out of the grid
btnZoomOut = Button(fOption, text = "Zoom out!", width = BTNWIDTH, command = lambda: tools.zoomOut(b))
btnZoomOut.grid(sticky =" n", pady = (10,0))

# Button Gosper Glider Gun: generates Gosper glider initial cell positions
btnGGG = Button(fOption, text = "Gosper Glide Gun!", width = BTNWIDTH, command = lambda: tools.ggg(b))
btnGGG.grid(sticky =" n", pady = (10,0))

# Label to display generations
lblGen = Label(fOption, text = "Generation: 0", fg = "white", bg = Board.BG)

# Button evolve (evolve only one generation)
btnEvolve = Button(fOption, text = "Evolve!", width = BTNWIDTH, command = lambda: tools.evolve(b, lblGen))
btnEvolve.grid(sticky = "n", pady = (10,0))

# Button Animation: evolving to infinity
btnAnim = Button(fOption, text = "Animate!", width = BTNWIDTH, command = lambda: tools.anim(b, lblGen))
btnAnim.grid(sticky = "n", pady = (10,0))

# Button Stop: to stop the animation
btnStop = Button(fOption, text = "Stop!", width = BTNWIDTH, command = lambda: tools.stop(b))
btnStop.grid(sticky = "n", pady = (10,0))

# Button Reset: reinitiate all cells and generation
btnReset = Button(fOption, text = "Reset!", width = BTNWIDTH, command = lambda: tools.reset(b, lblGen))
btnReset.grid(sticky = "n", pady = (10,0))

lblGen.grid(sticky = "n", pady = (10,0))

fOption.grid_columnconfigure(0, weight = 1)
fOption.grid_columnconfigure(0, weight = 1)

root.rowconfigure(0, weight = 1)
root.columnconfigure(1, weight = 1)

# Launching
root.mainloop()