import os
import pygame
from .constant import *


black=[b_bishop,b_king,b_knight,b_pawn,b_queen,b_rook]
white=[w_bishop,w_king,w_knight,w_pawn,w_queen,w_rook]

B=[]
W=[]

for img in black:
    B.append(pygame.transform.scale(img,(55,55)))


for img in white:
    W.append(pygame.transform.scale(img,(55,55)))    
class Piece():
    img=-1
    rect=(113,113,525,525)
    startX=rect[0]
    startY=rect[1]
    def __init__(self,row,col,color):
        self.row=row
        self.col=col
        self.color=color
        self.selected=False
        self.king=False
        self.pawn=False
        self.moves=[]

    def isSelected(self):
        return self.selected
    
    def update_valid_moves(self,board):
        self.moves=self.valid_moves(board)
    
    def Draw(self,win,color):
        if self.color=="w":
            drawimg=W[self.img]
        else:
            drawimg=B[self.img]

        x=(4-self.col)+round(self.startX+(self.col*self.rect[2]/8))
        y=3+round(self.startY+(self.row*self.rect[3]/8))

        if self.selected and self.color==color:
            pygame.draw.rect(win,(255,0,0),(x,y,62,62),4)

        win.blit(drawimg,(x,y))  

    def change_pos(self,pos):
        self.row=pos[0]
        self.col=pos[1]

    def __str__(self):
        return str(self.col)+" "+str(self.row)      

class Bishop(Piece):
    img=0
    def valid_moves(self,board):
        i=self.row
        j=self.col

        moves=[]
        
        #top right
        diL=j+1
        diR=j-1

        for D in range(i-1,-1,-1):
            if diL<8:
                p=board[D][diL]
                if p==0:
                    moves.append((diL,D))
                elif p.color!=self.color:
                    moves.append((diL,D))
                else:
                    break
            else:
                break
            diL+=1

        for D in range(i-1,-1,-1):
            if diR>-1:
                p=board[D][diR]
                if p==0:
                    moves.append((diR,D))
                elif p.color!=self.color:
                    moves.append((diR,D))
                else:
                    break
            else:
                break
            diR-=1

        #top left 
        diL=j+1
        diR=j-1
        for D in range(i+1,8):
            if diL<8:
                p=board[D][diL]
                if p==0:
                    moves.append((D,diL))
                elif p.color!=self.color:
                    moves.append((D,diL))
                else:
                    break
            else:
                break
            diL+=1

        for D in range(i+1,8):
            if diR>-1:
                p=board[D][diR]
                if p==0:
                    moves.append((D,diR))
                elif p.color!=self.color:
                    moves.append((D,diR))
                else:
                    break
            else:
                break
            diR-=1

        return moves

class king(Piece):
    img=1

    def __init__(self,row,col,color):
        super().__init__(row,col,color)
        self.king=True

    def valid_moves(self,board):
        moves=[]

        i=self.row
        j=self.col
        if i>0:

            #top left
            if j>0:
                p=board[i-1][j-1]
                if p==0:
                    moves.append((j-1,i-1))
                elif p.color!=self.color:
                    moves.append((j-1,i-1))
                
             #top middel 
            p=board[i-1][j]
            if p==0:
                moves.append((j,i-1))
            elif p.color!=self.color:
                moves.append((j,i-1))

            #top right
            if j<7:
                p=board[i-1][j+1]
                if p==0:
                    moves.append((j+1,i-1))
                elif p.color!=self.color:
                    moves.append((j+1,i-1))
            
        #bottom left
        if i<7:
            if j>0:
                p=board[i+1][j-1]
            if p==0:
                moves.append((j-1,i+1))
            elif p.color!=self.color:
                moves.append((j-1,i+1))

            #bottom middle
            p=board[i+1][j]
            if p==0:
                moves.append((j,i+1))
            elif p.color!=self.color:
                moves.append((j,i+1))

            #bottom right
            if j<7:
                p=board[i+1][j+1]
            if p==0:
                moves.append((j+1,i+1))
            elif p.color!=self.color:
                moves.append((j+1,i+1))

        #middle left
        if j>0:
            p=board[i][j-1]
            if p==0:
                moves.append((j-1,i))
            elif p.color!=self.color:
                moves.append((j-1,i))

        #middle right
        if j<7:
            p=board[i][j+1]
            if p==0:
                moves.append((j+1,i))
            elif p.color!=self.color:
                moves.append((j+1,i))

        return moves

class Knight(Piece):
    img=2
    def valid_moves(self,board):
        moves=[]    
        i=self.row
        j=self.col

        #top left
        if i>1 and j>0:
            p=board[i-2][j-1]
            if p==0:
                moves.append((j-1,i-2))
            elif p.color!=self.color:
                moves.append((j-1,i-2))
            
        #bottom left
        if i<6 and j>7:
            p=board[i+2][j-1]
            if p==0:
                moves.append((j-1,i-2))
            elif p.color!=self.color:
                moves.append((j-1,i-2))

        #top right
        if i>1 and j<7:
            p=board[i-2][j+1]
            if p==0:
                moves.append((j+1,i-2))
            elif p.color!=self.color:
                moves.append((j+1,i-2))

        #bottom right
        if i<6 and j<7:
            p=board[i+2][j+1]
            if p==0:
                moves.append((j+1,i+2))
            elif p.color!=self.color:
                moves.append((j+1,i+2))


        if i>0 and j>1:
            p=board[i-1][j-2]
            if p==0:
                moves.append((j-2,i-1))
            elif p.color!=self.color:
                moves.append((j-2,i-1))

        if i>0 and j<6:
            p=board[i-1][j+2]
            if p==0:
                moves.append((j+2,i-1))
            elif p.color!=self.color:
                moves.append((j+2,i-1))

        if i < 7 and j > 1:
            p = board[i + 1][j - 2]
            if p == 0:
                moves.append((j - 2, i + 1))
            elif p.color != self.color:
                moves.append((j - 2, i + 1))

        if i < 7 and j < 6:
            p = board[i + 1][j + 2]
            if p == 0:
                moves.append((j + 2, i + 1))
            elif p.color != self.color:
                moves.append((j + 2, i + 1))

        return moves        

class Pawn(Piece):
    img=3
    def __init__(self,row,col,color):
        super().__init__(row,col,color)
        self.queen=False
        self.first=True
        self.pawn=True
        
    def valid_moves(self,board):
        i=self.row
        j=self.col
        moves=[]

        try:
            if self.color =='b':
                if i<7:
                    p=board[i+1][j]
                    if p==0:
                        moves.append((j,i+1))
                    
                    #diagonal
                    if j<7:
                        p=board[i+1][j+1]
                        if p!=0:
                            if p.color!=self.color:
                                moves.append((j+1,i+1))

                    if j>0:
                        p=board[i+1][j-1]
                        if p!=0:
                            if p.color !=self.color:
                                moves.append((j-1,i+1))

                if self.first:
                    if i<6:
                        p=board[i+2][j]
                        if p==0:
                            if board[i + 1][j] == 0:
                                moves.append((j, i + 2))
                        elif p.color != self.color:
                            moves.append((j,i+2))
                        
            else:
                if i>0:
                    p=board[i-1][j]
                    if p==0:
                        moves.append((j,i-1))
                if j<7:
                    p=board[i-1][j+1]
                    if p!=0:
                        if p.color!= self.color:
                            moves.append((j+1,i-1))  

                if j>0:
                    p=board[i-1][j-1]
                    if p!=0:
                        if p.color !=self.color:
                            moves.append((j-1,i-1))
                
                if self.first:
                    if i>1:
                        p=board[i-2][j]
                        if p==0:
                            if board[i-1][j]==0:
                                moves.append((j,i-2))
                        elif p.color!=self.color:
                            moves.append((j,i-2))
        except:
            pass
        return moves

class Queen(Piece):
    img=4
    def valid_moves(self,board):
        i = self.row
        j = self.col

        moves = []

        # TOP RIGHT
        djL = j + 1
        djR = j - 1
        for di in range(i - 1, -1, -1):
            if djL < 8:
                p = board[di][djL]
                if p == 0:
                    moves.append((djL, di))
                elif p.color != self.color:
                    moves.append((djL, di))
                    break
                else:
                    djL = 9

            djL += 1

        for di in range(i - 1, -1, -1):
            if djR > -1:
                p = board[di][djR]
                if p == 0:
                    moves.append((djR, di))
                elif p.color != self.color:
                    moves.append((djR, di))
                    break
                else:
                    djR = -1

            djR -= 1

        # TOP LEFT
        djL = j + 1
        djR = j - 1
        for di in range(i + 1, 8):
            if djL < 8:
                p = board[di][djL]
                if p == 0:
                    moves.append((djL, di))
                elif p.color != self.color:
                    moves.append((djL, di))
                    break
                else:
                    djL = 9
            djL += 1
        for di in range(i + 1, 8):
            if djR > -1:
                p = board[di][djR]
                if p == 0:
                    moves.append((djR, di))
                elif p.color != self.color:
                    moves.append((djR, di))
                    break
                else:
                    djR = -1

            djR -= 1

        # UP
        for x in range(i - 1, -1, -1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break

        # DOWN
        for x in range(i + 1, 8, 1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break

        # LEFT
        for x in range(j - 1, -1, -1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.color != self.color:
                moves.append((x, i))
                break
            else:
                break

        # RIGHT
        for x in range(j + 1, 8, 1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.color != self.color:
                moves.append((x, i))
                break
            else:
                break

        return moves
    

class Rook(Piece):
    img=5
    def valid_moves(self,board):
        i= self.row
        j=self.col

        moves=[]

        #up
        for a in range(i-1,-1,-1):
            p=board[a][j]
            if p==0:
                moves.append((j,a))
            elif p.color !=self.color:
                moves.append((j,a))
                break
            else:
                break
        
        #down
        for a in range(i+1,8,1):
            p=board[a][j]
            if p==0:
                moves.append((j,a))
            elif p.color!= self.color:
                moves.append((j,a))
                break
            else:
                break

        #left 
        for a in range(j-1,-1,-1):
            p=board[i][a]
            if p==0:
                moves.append((a,i))
            elif p.color!= self.color:
                moves.append((a,i))
                break
            else:
                break
        
        #right
        for a in range(j+1,8,1):
            p=board[i][a]
            if p==0:
                moves.append((a,i))
            elif p.color!= self.color:
                moves.append((a,i))
                break
            else:
                break
        
        return moves