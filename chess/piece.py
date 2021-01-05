import os
import pygame
from .constant import WHITE,BLACK

b_bishop = pygame.image.load(os.path.join("img", "black_bishop.png"))
b_king = pygame.image.load(os.path.join("img", "black_king.png"))
b_knight = pygame.image.load(os.path.join("img", "black_knight.png"))
b_pawn = pygame.image.load(os.path.join("img", "black_pawn.png"))
b_queen = pygame.image.load(os.path.join("img", "black_queen.png"))
b_rook = pygame.image.load(os.path.join("img", "black_rook.png"))

w_bishop = pygame.image.load(os.path.join("img", "white_bishop.png"))
w_king = pygame.image.load(os.path.join("img", "white_king.png"))
w_knight = pygame.image.load(os.path.join("img", "white_knight.png"))
w_pawn = pygame.image.load(os.path.join("img", "white_pawn.png"))
w_queen = pygame.image.load(os.path.join("img", "white_queen.png"))
w_rook = pygame.image.load(os.path.join("img", "white_rook.png"))

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
                pass
