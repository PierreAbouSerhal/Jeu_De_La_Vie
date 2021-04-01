import tkinter as tk
from tkinter import Canvas
from cell import Cell

class Board:

    BG      = "grey30"
    BGALIVE = "red"
    BGDEAD  = "white"

    def __init__(self, frame, cellD=70, col=10, row=10):
        ''' Board have 3 argumetns:
            root:  root window
            cellD: single Cell Dimentions
            col:   number of columns
            row:   number of rows '''
        self.cellD  = cellD
        self.col    = col
        self.row    = row
        self.width  = self.cellD * self.col
        self.height = self.cellD * self.row
        self.cells  = {} # Dictionnary that contains all cells and their positions

        # creating all initial cells
        for i in range(self.row):
            for j in range(self.col):
                cell = Cell()
                self.cells[i,j] = cell

        self.canv   = Canvas(frame, width=self.width, height=self.height, bg=self.BG) # Canvas that will contain the game grid
        
    def setCol(self, col):
        self.col = col
    
    def setRow(self, row):
        self.row = row

    def setCellD(self, cellD):
        self.cellD = cellD

    def drawBoard(self):
        ''' Draws th board and returns the canvas '''

        self.gridCells  = {} # Dictionnary that contains all grid cells

        cellD  = self.cellD
        width  = self.width
        height = self.height
        canvas = self.canv

        x1, y1 = 0, 0
        x2, y2 = cellD, cellD

        for y in range(self.row):

            for x in range(self.col):
                
                # Resurect or kill cell
                if self.cells[y,x].nbrs == 3:
                    self.cells[y,x].live()
                elif self.cells[y,x].nbrs == 2:
                    if not self.cells[y,x].isAlive:
                        self.cells[y,x].die()
                    else:
                        self.cells[y,x].live()
                elif self.cells[y,x].nbrs < 2 or self.cells[y,x].nbrs > 3:
                    self.cells[y,x].die()

                gridCell = canvas.create_rectangle(x1, y1, x2, y2, fill= self.BGALIVE if self.cells[y,x].isAlive else self.BGDEAD, outline="black")
                self.cells[y,x].clickCnt = 1 if self.cells[y,x].isAlive else 0
                canvas.tag_bind(gridCell, '<Button-1>', self.onCellClick) # On click listener for each gridCell in the board 

                self.gridCells[(int(y1/cellD), int(x1/cellD))] = gridCell # Storing all grid cells to access them
            
                x1 = x1 + cellD
                x2 = x2 + cellD

            x1 = 0
            x2 = cellD
            y1 = y1 + cellD
            y2 = y2 + cellD

        canvas.pack(side=tk.TOP, anchor=tk.NW)
        return canvas

    def onCellClick(self, event):
        ''' On cell grid click listener '''
        x = int(event.x/self.cellD)
        y = int(event.y/self.cellD)
        
        # Switching cell collor
        self.canv.itemconfig(self.gridCells[(y, x)], fill = self.BGALIVE if self.cells[y,x].clickCnt % 2 == 0 else self.BGDEAD)

        self.cells[y,x].clickCnt = self.cells[y,x].clickCnt + 1

        self.cells[y,x].isAlive  = not self.cells[y,x].isAlive