from tkinter import * 
from tkinter.ttk import *
import tkinter as tk
from cell import Cell

FIXED_HEIGHT = 700
DIVISORS     = [1, 2, 4, 5, 7, 10, 14, 20, 25, 28, 35, 50, 70, 100, 140, 175, 350, 700]
DIVIDX       = 1

def zoomIn(board):
    ''' Zoom in the grid (in reality we are reducing the number of grid cells) 
        Takes the game board as parameter'''
    global DIVIDX
    
    boardRow = 0
    boardCol  = 0

    if DIVIDX == 0:
        return

    for divisor in DIVISORS:
        if FIXED_HEIGHT / board.cellD == divisor:
            DIVIDX = DIVISORS.index(divisor)

    DIVIDX = DIVIDX - 1 

    board.setCellD(FIXED_HEIGHT / DIVISORS[DIVIDX])

    colCnt = int(FIXED_HEIGHT / board.cellD)
    rowCnt = colCnt

    board.setCol(colCnt)
    board.setRow(rowCnt)

    temp = board.cells
    
    board.cells = {}

    for i in range(rowCnt):
        for j in range(colCnt):
            cell = Cell()
            board.cells[i,j] = cell

    for i in range(rowCnt):
        for j in range(rowCnt):
            if temp[i,j].isAlive:
                board.cells[i,j] = temp[i,j]

    board.canv.delete("all")
    board.drawBoard()

def zoomOut(board):
    ''' Zoom out of the grid (in reality we are increasing the number of grid cells) 
        Takes the game board as parameter '''
    global DIVIDX
    
    if DIVIDX == len(DIVISORS) - 1:
        return

    for divisor in DIVISORS:
        if FIXED_HEIGHT / board.cellD == divisor:
            DIVIDX = DIVISORS.index(divisor)

    DIVIDX = DIVIDX + 1 

    board.setCellD(FIXED_HEIGHT / DIVISORS[DIVIDX])

    colCnt = int(FIXED_HEIGHT / board.cellD)
    rowCnt = int(FIXED_HEIGHT / board.cellD)

    oldRowCnt = board.row
    oldColCnt = board.col

    board.setCol(colCnt)
    board.setRow(rowCnt)

    temp = board.cells

    board.cells = {}

    for i in range(rowCnt):
        for j in range(colCnt):
            cell = Cell()
            board.cells[i,j] = cell

    for i in range(oldRowCnt):
        for j in range(oldColCnt):
            if temp[i,j].isAlive:
                board.cells[i,j] = temp[i,j]

    board.canv.delete("all")
    board.drawBoard()

def evolve(board):
    ''' Evaluate which cell lives or dies each generation'''
    cells  = board.cells
    rowCnt = board.row - 1 # We substracted 1 because grid will begin at index 0
    colCnt = board.col - 1 # We substracted 1 because grid will begin at index 0

    for y in range(board.row):

        for x in range(board.col):

            # Secial cases: grid borders

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

    board.drawBoard()
    #board.canv.after(1000, evolve())