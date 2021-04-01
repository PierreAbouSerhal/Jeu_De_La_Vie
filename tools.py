from tkinter import * 
from tkinter.ttk import *
import tkinter as tk

FIXED_HEIGHT = 700
DIVISORS     = [1, 2, 4, 5, 7, 10, 14, 20, 25, 28, 35, 50, 70, 100, 140, 175, 350, 700]
DIVIDX       = 1

def zoomIn(board):
    global DIVIDX
    
    boardRow = 0
    boardCol  = 0

    if DIVIDX == 0:
        return

    for divisor in DIVISORS:
        if FIXED_HEIGHT / board.cellD == divisor:
            DIVIDX = DIVISORS.index(divisor)

    DIVIDX = DIVIDX - 1 

    board.cellD = FIXED_HEIGHT / DIVISORS[DIVIDX]

    colCnt = int(FIXED_HEIGHT / board.cellD)
    rowCnt = colCnt

    board.col = colCnt
    board.row = rowCnt

    temp = board.grid
    
    board.grid = [ [0]*rowCnt for n in range(colCnt) ]

    for i in range(rowCnt):
        for j in range(rowCnt):
            if temp[i][j] == 1:
                board.grid[i][j] = 1

    board.canv.delete("all")
    board.drawBoard()

def zoomOut(board):
    global DIVIDX
    
    if DIVIDX == len(DIVISORS) - 1:
        return

    for divisor in DIVISORS:
        if FIXED_HEIGHT / board.cellD == divisor:
            DIVIDX = DIVISORS.index(divisor)

    DIVIDX = DIVIDX + 1 

    board.cellD = FIXED_HEIGHT / DIVISORS[DIVIDX]

    colCnt = int(FIXED_HEIGHT / board.cellD)
    rowCnt = int(FIXED_HEIGHT / board.cellD)

    board.col = colCnt
    board.row = colCnt

    temp = board.grid

    board.grid = [ [0]*rowCnt for n in range(colCnt) ]

    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if temp[i][j] == 1:
                board.grid[i][j] = 1

    board.canv.delete("all")
    board.drawBoard()

    def evolve(aCelPos):
        # Check if 
        if not bool(acelPos): 
            return
        
        for pos in aCelPos:
            celY = pos[0]
            celX = pos[1]

            y = 0 if celY = 0 else celY - 1
            x = 0 if celX = 0 else celX - 1

            cell = aCelPos[pos]

            while celY < celY + 2:

                
