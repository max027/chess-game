import pygame
import os
import time
from chess.constant import HEIGHT,WIDTH,board,chessbg,ROWS,COLS
from chess.board import Board
from chess.piece import Piece
FPS=60
WINDOW=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Chess")
clock=pygame.time.Clock()
turn="w"
from chess.piece  import  Piece

def main():
    global  chessbg
    WINDOW.blit(chessbg, (0, 0))
    pygame.display.update()
    time.sleep(3)
    run=True
    clock.tick(FPS)
    for i in range(ROWS):
        for j in range(COLS):
            piece=Piece(i,j,"w")
            piece.Draw(WINDOW,turn)
    while(run):
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run=False
        for i in range(ROWS):
            for j in range(COLS):
                piece = Piece(i, j, "w")
                piece.Draw(WINDOW, turn)
        WINDOW.blit(board,(0,0))
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()