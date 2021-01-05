import pygame
from chess.constant import HEIGHT,WIDTH
from chess.board import Board
from chess.piece import Piece
FPS=60
WINDOW=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Chess")
clock=pygame.time.Clock()

def main():
    run=True
    clock.tick(FPS)
    board=Board()
    while(run):
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run=False
        
        board.draw(WINDOW)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()