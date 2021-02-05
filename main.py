import pygame
from chess.constant import HEIGHT,WIDTH,board
from chess.board import Board
from chess.piece import Piece
FPS=60
WINDOW=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Chess")
clock=pygame.time.Clock()


def main():
    
    run=True
    clock.tick(FPS)
    while(run):
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run=False
        
        WINDOW.blit(board,(0,0))
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()