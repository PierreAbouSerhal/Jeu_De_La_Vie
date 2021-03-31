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

    for row in temp:
        for col in row:
            if col == 1:
                board.grid[boardRow][boardCol] = 1
                boardCol = boardCol + 1
        boardRow = boardRow + 1

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

    for row in temp:
        for col in row:
            if col == 1:
                board.grid[temp.index(row)][row.index(col)] = 1

    board.canv.delete("all")
    board.drawBoard()