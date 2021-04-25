from tkinter import * 
from tkinter.ttk import *
import tkinter as tk
from cell import Cell
from time import sleep

# The game grid is a square of dimension = 700px 
FIXED_DIMENSION = 700 

# All divisors of 700: To properly fill all of the canvas with cells 
DIVISORS = [1, 2, 4, 5, 7, 10, 14, 20, 25, 28, 35, 50, 70, 100, 140, 175, 350, 700]

# Variable used to calculate number of cells in the board
divIdx = 1

# Number of generations
genCnt = 0

def zoomIn(board):
    ''' Zoom in the grid (in reality we are reducing the number of grid cells) 
        Takes the game board as parameter'''
    global divIdx
    board.zoom = True # if zoom, board will save cell states without evolving 

    if divIdx == 0: # Prevent index exception
        return

    # Calculate current board dimension
    for divisor in DIVISORS:
        if FIXED_DIMENSION / board.cellD == divisor:
            divIdx = DIVISORS.index(divisor)

    # New board dimension 
    divIdx = divIdx - 1 

    # Update cell dimension
    board.setCellD(FIXED_DIMENSION / DIVISORS[divIdx])

    colCnt = int(FIXED_DIMENSION / board.cellD)
    rowCnt = colCnt

    board.setCol(colCnt)
    board.setRow(rowCnt)

    # temp is used preserve cell state
    temp = board.cells
    
    board.cells = {}

    # Reinitiate board cells
    for i in range(rowCnt):
        for j in range(colCnt):
            cell = Cell()
            board.cells[i,j] = cell

    # Resurecting cells
    for i in range(rowCnt):
        for j in range(rowCnt):
            if temp[i,j].isAlive:
                board.cells[i,j] = temp[i,j]

    board.canv.delete("all")
    board.drawBoard()

    board.zoom = False

def zoomOut(board):
    ''' Zoom out of the grid (in reality we are increasing the number of grid cells) 
        Takes the game board as parameter '''
    global divIdx

    board.zoom = True # if zoom, board will save cell states without evolving 

    if divIdx == len(DIVISORS) - 1: # Prevent index exception
        return

    # Calculate current board dimension
    for divisor in DIVISORS:
        if FIXED_DIMENSION / board.cellD == divisor:
            divIdx = DIVISORS.index(divisor)

    # New board dimension 
    divIdx = divIdx + 1 

    # Updating cell dimension 
    board.setCellD(FIXED_DIMENSION / DIVISORS[divIdx])

    colCnt = int(FIXED_DIMENSION / board.cellD)
    rowCnt = int(FIXED_DIMENSION / board.cellD)

    oldRowCnt = board.row
    oldColCnt = board.col

    board.setCol(colCnt)
    board.setRow(rowCnt)

    # temp is used preserve cell state
    temp = board.cells

    board.cells = {}

    # Reinitiate board cells
    for i in range(rowCnt):
        for j in range(colCnt):
            cell = Cell()
            board.cells[i,j] = cell

    # Resurecting alive cells
    for i in range(oldRowCnt):
        for j in range(oldColCnt):
            if temp[i,j].isAlive:
                board.cells[i,j] = temp[i,j]

    board.canv.delete("all")
    board.drawBoard()

    board.zoom = False

def evolve(board, lblGen):
    ''' Evaluate which cell lives or dies each generation'''
    global genCnt

    cells  = board.cells
    rowCnt = board.row - 1 # We substracted 1 because grid will begin at index 0
    colCnt = board.col - 1 # We substracted 1 because grid will begin at index 0

    for cellXY in cells:
        y = cellXY[0]
        x = cellXY[1]
        #cell = cells[cellXY]

        # 1- Top left border
        if y == 0 and x == 0:
            nbrs = 0
            if cells[y,x+1].isAlive:
                nbrs += 1
            if cells[y+1, x].isAlive:
                nbrs += 1
            if cells[y+1, x+1].isAlive:
                nbrs += 1
            cells[y,x].nbrs = nbrs
        
        # 2- Top right corner
        elif y == 0 and x == colCnt:
            nbrs = 0
            if cells[y,x-1].isAlive:
                nbrs += 1
            if cells[y+1, x].isAlive:
                nbrs += 1
            if cells[y+1, x-1].isAlive:
                nbrs += 1
            cells[y,x].nbrs = nbrs
        
        # 3- Bottom left corner
        elif y == rowCnt and x == 0:
            nbrs = 0
            if cells[y-1,x].isAlive:
                nbrs += 1
            if cells[y-1, x+1].isAlive:
                nbrs += 1
            if cells[y, x+1].isAlive:
                nbrs += 1
            cells[y,x].nbrs = nbrs

        # 4- Bottom right corner
        elif y == rowCnt and x == colCnt:
            nbrs = 0
            if cells[y-1,x].isAlive:
                nbrs += 1
            if cells[y-1, x-1].isAlive:
                nbrs += 1
            if cells[y, x-1].isAlive:
                nbrs += 1
            cells[y,x].nbrs = nbrs

        # 5- Top border
        elif y == 0 and 0<x<colCnt :
            nbrs = 0
            if cells[y,x-1].isAlive:
                nbrs += 1
            if cells[y,x+1].isAlive:
                nbrs += 1
            if cells[y+1, x-1].isAlive:
                nbrs +=1
            if cells[y+1,x].isAlive:
                nbrs += 1
            if cells[y+1, x+1].isAlive:
                nbrs += 1
            cells[y,x].nbrs = nbrs

        # 6- Right border
        elif 0<y<rowCnt and x == colCnt:
            nbrs = 0
            if cells[y-1,x].isAlive:
                nbrs += 1
            if cells[y-1,x-1].isAlive:
                nbrs += 1
            if cells[y,x-1].isAlive:
                nbrs +=1
            if cells[y+1,x-1].isAlive:
                nbrs += 1
            if cells[y+1, x].isAlive:
                nbrs += 1
            cells[y,x].nbrs = nbrs

        # 7- Bottom border
        elif y == rowCnt and 0<x<colCnt :
            nbrs = 0
            if cells[y,x-1].isAlive:
                nbrs += 1
            if cells[y-1,x-1].isAlive:
                nbrs += 1
            if cells[y-1, x].isAlive:
                nbrs +=1
            if cells[y-1,x+1].isAlive:
                nbrs += 1
            if cells[y, x+1].isAlive:
                nbrs += 1
            cells[y,x].nbrs = nbrs

        # 8- Left border
        elif 0<y<rowCnt and x == 0:
            nbrs = 0
            if cells[y-1,x].isAlive:
                nbrs += 1
            if cells[y-1,x+1].isAlive:
                nbrs += 1
            if cells[y,x+1].isAlive:
                nbrs +=1
            if cells[y+1,x+1].isAlive:
                nbrs += 1
            if cells[y+1, x].isAlive:
                nbrs += 1
            cells[y,x].nbrs = nbrs
        
        # General cases: grid
        else:
            nbrs = 0
            if cells[y-1,x-1].isAlive:
                nbrs += 1
            if cells[y-1,x].isAlive:
                nbrs += 1
            if cells[y-1,x+1].isAlive:
                nbrs += 1
            if cells[y,x-1].isAlive:
                nbrs += 1
            if cells[y,x+1].isAlive:
                nbrs += 1
            if cells[y+1,x-1].isAlive:
                nbrs += 1
            if cells[y+1,x].isAlive:
                nbrs += 1
            if cells[y+1,x+1].isAlive:
                nbrs += 1
            cells[y,x].nbrs = nbrs

    # Refreshing the board
    board.refresh()
    
    # Updating generation label
    genCnt += 1
    lblGen.config(text="Generation: " + str(genCnt))

    if board.anim: 
        board.parent.after(50, evolve, board, lblGen)
    

def anim(board, lblGen):
    ''' Begin the animation '''
    board.anim = True
    evolve(board, lblGen)

def stop(board):
    ''' Stop the animation '''
    board.anim = False

def reset(board, lblGen):
    global genCnt

    board.anim = False
    board.cells = {}
    
    for i in range(board.row):
        for j in range(board.col):
            cell = Cell()
            board.cells[i,j] = cell

    genCnt = 0
    lblGen.config(text="Generation: " + str(genCnt))

    board.drawBoard()

def ggg(board):
    ''' Initiate the Gosper Glider Gun '''
    # Disable animation
    board.anim = False

    # Enable pattern drawing
    board.drawPattern = True
    
    # zoom out to fit the Canon
    while board.col <= 36:
        zoomOut(board)

    # Kill all the cells
    for cell in board.cells:
        board.cells[cell].die()

    # Gosper Glide Gun alive cell coordinates 
    glider_gun =[
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


    for y in range(len(glider_gun)):
        for x in range(len(glider_gun[y])):
            if glider_gun[y][x] == 1:
                board.cells[y,x].live()

    board.refresh()

    # Disable pattern drawing
    board.drawPattern = False