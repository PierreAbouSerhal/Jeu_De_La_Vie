import tkinter as tk
from tkinter import *
from cell import Cell

# Game board object
class Board:

    BG      = "grey30"
    BGALIVE = "red"
    BGDEAD  = "white"

    def __init__(self, frame, cellD=70, col=10, row=10):
        ''' Board have 3 argumetns:
            frame:  parent of the canvas
            cellD: single Cell Dimentions
            col:   number of columns
            row:   number of rows '''
        self.cellD  = cellD
        self.col    = col
        self.row    = row
        self.width  = self.cellD * self.col
        self.height = self.cellD * self.row
        self.parent = frame # Parent of the canvas that will contain the grid 
        self.zoom   = False # Boolean that is used to zoom in or out of the boeard witout destroying all cells
        self.anim   = False # Boolean that is used to stop or begin the animation
        self.drawPattern = False # Boolean that is used to draw known cellular pattern 
        self.cells  = {}    # Dictionnary that contains all cells and their positions

        # creating all initial cells
        for i in range(self.row):
            for j in range(self.col):
                cell = Cell()
                self.cells[i,j] = cell

        self.canv   = Canvas(frame, width=self.width, height=self.height, bg=self.BG) # Canvas that will contain the game grid
        
    # setters
    def setCol(self, col):
        self.col = col
    
    def setRow(self, row):
        self.row = row

    def setCellD(self, cellD):
        self.cellD = cellD

    def refresh(self):
        ''' Refresh the board '''

        for cellXY in self.cells:
            y = cellXY[0]
            x = cellXY[1]
            cell = self.cells[cellXY]

            if not self.drawPattern:
                # Resurect or kill cell
                if cell.nbrs == 3:
                    cell.live()
                elif cell.nbrs == 2:
                    if not cell.isAlive:
                        cell.die()
                    else:
                        cell.live()
                elif cell.nbrs < 2 or cell.nbrs > 3:
                    cell.die()

            self.canv.itemconfig(self.gridCells[(y, x)], fill = self.BGALIVE if cell.isAlive else self.BGDEAD)

            cell.clickCnt = 1 if cell.isAlive else 0

    def drawBoard(self):

        self.gridCells  = {} # Dictionnary that contains all grid cells

        cellD  = self.cellD
        canvas = self.canv
        cells  = self.cells
        zoom   = self.zoom
        gridD  = self.col - 1

        x1, y1 = 0, 0
        x2, y2 = cellD, cellD

        # Drawing board rectangles
        for cellXY in cells:
            y = cellXY[0]
            x = cellXY[1]
            cell = cells[cellXY]
            
            # Preserve all cell states when zooming: zoom = True
            if not zoom: 
                # Resurect or kill cell
                if cell.nbrs == 3:
                    cell.live()
                elif cell.nbrs == 2:
                    if not cell.isAlive:
                        cell.die()
                    else:
                        cell.live()
                elif cell.nbrs < 2 or cell.nbrs > 3:
                    cell.die()

            # Creationg the canvas
            gridCell = canvas.create_rectangle(x1, y1, x2, y2, fill= self.BGALIVE if self.cells[y,x].isAlive else self.BGDEAD, outline="black")

            self.cells[y,x].clickCnt = 1 if self.cells[y,x].isAlive else 0 # Keep the click funtionnality working

            canvas.tag_bind(gridCell, '<Button-1>', self.onCellClick) # On click listener for each gridCell in the board 

            self.gridCells[(int(y1/cellD), int(x1/cellD))] = gridCell # Storing all grid cells to access them and change color

            # Updating rectangles coordinates
            x1 = x1 + cellD
            x2 = x2 + cellD

            if x == gridD:
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

        # Updating click count
        self.cells[y,x].clickCnt = self.cells[y,x].clickCnt + 1

        # Kill or resurect a cell
        self.cells[y,x].isAlive  = not self.cells[y,x].isAlive