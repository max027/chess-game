import pygame
from piece import Bishop
from piece import king
from piece import Knight
from piece import Pawn
from piece import Queen
from piece import Rook 
from .constant import *

class Board():
        rect=(113,113,525,525)
        startX=rect[0]
        startY=rect[1]
        def __init__(self,row,col):
                self.row=row
                self.col=col
                self.ready=False
                self.board=[[0 for i in range(8)] for _ in range(row)]

                self.board[0][0]=Rook(0,0,"b")
                self.board[0][1]=Knight(0,1,"b")
                self.board[0][2]=Bishop(0,2,"b")
                self.board[0][3]=Queen(0,3,"b")
                self.board[0][4]=king(0,4,"b")
                self.board[0][5]=Bishop(0,5,"b")
                self.board[0][6]=Knight(0,6,"b")
                self.board[0][7]=Rook(0,7,"b")


                self.board[1][0]=Pawn(1,0,"b")
                self.board[1][1]=Pawn(1,1,"b")      
                self.board[1][2]=Pawn(1,2,"b")      
                self.board[1][3]=Pawn(1,3,"b")      
                self.board[1][4]=Pawn(1,4,"b")      
                self.board[1][5]=Pawn(1,5,"b")      
                self.board[1][6]=Pawn(1,6,"b")      
                self.board[1][7]=Pawn(1,7,"b")      


                self.board[7][0]=Rook(7,0,"w")
                self.board[7][1]=Knight(7,1,"w")
                self.board[7][2]=Bishop(7,2,"w")
                self.board[7][3]=Queen(7,3,"w")
                self.board[7][4]=king(7,4,"w")
                self.board[7][5]=Bishop(7,5,"w")
                self.board[7][6]=Knight(7,6,"w")
                self.board[7][7]=Rook(7,7,"w")


                self.board[6][0]=Pawn(6,0,"w")
                self.board[6][1]=Pawn(6,1,"w")      
                self.board[6][2]=Pawn(6,2,"w")      
                self.board[6][3]=Pawn(6,3,"w")      
                self.board[6][4]=Pawn(6,4,"w")      
                self.board[6][5]=Pawn(6,5,"w")      
                self.board[6][6]=Pawn(6,6,"w")      
                self.board[6][7]=Pawn(6,7,"w")

                self.p1name="player 1"
                self.p2name="player 2"
                self.turn="w"
                self.winner=None
                self.last=None
        def update_moves(self):
                for i in range(self.row):
                        for j in range(self.col):
                                if self.board[i][j]!=0:
                                        self.board[i][j].update_valid_moves(self.board)
