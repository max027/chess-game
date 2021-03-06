import pygame
from .piece import Bishop
from .piece import king
from .piece import Knight
from .piece import Pawn
from .piece import Queen
from .piece import Rook 
import time
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
                self.starttime=time.time()

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
                self.storedTime1 = 0
                self.storedTime2 = 0

        def update_moves(self):
                for i in range(self.row):
                        for j in range(self.col):
                                if self.board[i][j]!=0:
                                        self.board[i][j].update_valid_moves(self.board)

        def draw(self,win,color):
                if self.last and color==self.turn:
                        y,x=self.last[0]
                        y1,x1=self.last[1]

                        xx = (4 - x) +round(self.startX + (x * self.rect[2] / 8))
                        yy = 3 + round(self.startY + (y * self.rect[3] / 8))
                        pygame.draw.circle(win, (0,0,255), (xx+32, yy+30), 34, 4)
                        xx1 = (4 - x) + round(self.startX + (x1 * self.rect[2] / 8))
                        yy1 = 3+ round(self.startY + (y1 * self.rect[3] / 8))
                        pygame.draw.circle(win, (0, 0, 255), (xx1 + 32, yy1 + 30), 34, 4)

                s=None
                for i in range(self.row):
                        for j in range(self.col):
                                if self.board[i][j]!=0:
                                        self.board[i][j].draw(win,color)
                                        if self.board[i][j].isSelected:
                                                s=(i,j) 

        def danger_moves(self,color):
                danger_move=[]
                for i in range(self.row):
                        for j in range(self.col):
                                if self.board[i][j]!=0:
                                        if self.board[i][j].color!=color:
                                                for move in self.board[i][j].moves:
                                                        danger_move.append(move)
                return danger_move
        
        
        def is_checked(self,color):
                self.update_moves()
                danger_move=self.danger_moves(color)
                king_pos=(-1,-1)
                for i in range(self.row):
                        for j in range(self.col):
                                if self.board[i][j]!=0:
                                        king_pos=(j,i)
                
                if king_pos in danger_move:
                        
                        return True
                
                return False
        
        def select(self,col,row,color):
                changed=False
                prev=(-1,-1)
                for i in range(self.row):
                        for j in range(self.col):
                                if self.board[i][j]!=0:
                                        if self.board[i][j].selected:
                                                prev=(i,j)
                
                if self.board[row][col]==0 and prev !=(-1,-1):
                        piece_moves=self.board[prev[0]][prev[1]].moves
                        if (col,row) in piece_moves:
                                changed=self.move(prev,(row,col),color)
                else:
                        if prev == (-1,-1):
                              self.reset_selected()
                              if self.board[row][col] != 0:
                                     self.board[row][col].selected = True

                        else:
                                if self.board[prev[0]][prev[1]].color != self.board[row][col].color:
                                        moves = self.board[prev[0]][prev[1]].moves
                                        if (col, row) in piece_moves:
                                                changed = self.move(prev, (row, col), color)
                                        if self.board[row][col].color == color:
                                                self.board[row][col].selected = True       
#---------------------------------
                                else:
                                        if self.board[row][col].color == color:
                                                #castling
                                                self.reset_selected()
                                                if self.board[prev[0]][prev[1]].moved == False and self.board[prev[0]][prev[1]].rook and self.board[row][col].king and col != prev[1] and prev!=(-1,-1):
                                                      castle = True     
                                                      if prev[1] < col:
                                                                for j in range(prev[1]+1, col):
                                                                       if self.board[row][j] != 0:
                                                                        castle = False

                                                                if castle:
                                                                     changed = self.move(prev, (row, 3), color)
                                                                     changed = self.move((row,col), (row, 2), color)
                                                                if not changed:
                                                                     self.board[row][col].selected = True

                                                      else:
                                                                for j in range(col+1,prev[1]):
                                                                    if self.board[row][j] != 0:
                                                                        castle = False
                                                                
                                                                if castle:
                                                                        changed = self.move(prev, (row, 6), color)
                                                                        changed = self.move((row,col), (row, 5), color)
                                                                if not changed:
                                                                        self.board[row][col].selected = True

                                                else:
                                                        self.board[row][col].selected = True
                        if changed:

                                if self.turn == "w":
                                     self.turn = "b"
                                     self.reset_selected()
                                else:
                                     self.turn = "w"
                                     self.reset_selected()
#---------------------------------
        def reset_selected(self):
                for i in range(self.row):
                        for i in range(self.col):
                                if self.board[i][j]!=0:
                                        self.board[i][j].selected=False

        def check_mate(self):
                return False

        def move(self,start,end,color):
                checked_before=self.is_checked(color)
                changed=False
                nboard=self.board[:]
                if nboard[start[0]][start[1]].pawn:
                        nboard[start[0]][start[1]].first=False
                nboard[start[0]][start[1]].change_pos((end[0], end[1]))
                nboard[end[0]][end[1]] = nboard[start[0]][start[1]]
                nboard[start[0]][start[1]] = 0
                self.board = nboard

                if self.is_checked(color) or (checked_before and self.is_checked(color)):
                        changed=False
                        nboard=self.board[:]
                        if nboard[end[0]][end[1]].pawn:
                                nBoard[end[0]][end[1]].first = True
                        
                        nboard[end[0]][end[1]].change_pos((start[0], start[1]))
                        nboard[start[0]][start[1]] = nboard[end[0]][end[1]]
                        nboard[end[0]][end[1]] = 0
                        self.board = nboard

                else:
                        self.reset_selected()
                self.update_moves()
                """
                if changed:
                        self.last=[start,end]
                        if self.turn=="w":
                                self.storedTime1 += (time.time() - self.starttime)
                        else:
                                self.storedTime2 += (time.time() - self.startTime)
                        self.startTime = time.time()
                """
                return changed


