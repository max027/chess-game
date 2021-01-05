import pygame
from .constant import *
class Board():
        def __init__(self):
                self.board=[]
                self.selected=False
                self.turn=0

        def draw(self,win):
                win.fill(BLACK)
                for row in range(ROWS):
                        for col in range(row%2,ROWS,2):
                                pygame.draw.rect(win,WHITE,(row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
        
        def draw_board(self):
                pass    