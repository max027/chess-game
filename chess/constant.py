import pygame
import os


WIDTH,HEIGHT=800,800
ROWS,COLS=8,8
SQUARE_SIZE=WIDTH   //COLS
WHITE=(244,164,96)
BLACK=(210,105,30)


b_bishop = pygame.image.load("/home/saurabh/programming/python_file/chess_game/chess/images/black_bishop.png")
b_king = pygame.image.load("/home/saurabh/programming/python_file/chess_game/chess/images/black_king.png")
b_knight = pygame.image.load("/home/saurabh/programming/python_file/chess_game/chess/images/black_knight.png")
b_pawn = pygame.image.load("/home/saurabh/programming/python_file/chess_game/chess/images/black_pawn.png")
b_queen = pygame.image.load("/home/saurabh/programming/python_file/chess_game/chess/images/black_queen.png")
b_rook = pygame.image.load("/home/saurabh/programming/python_file/chess_game/chess/images/black_rook.png")

w_bishop = pygame.image.load("/home/saurabh/programming/python_file/chess_game/chess/images/white_bishop.png")
w_king = pygame.image.load("/home/saurabh/programming/python_file/chess_game/chess/images/white_king.png")
w_knight = pygame.image.load("/home/saurabh/programming/python_file/chess_game/chess/images/white_knight.png")
w_pawn = pygame.image.load("/home/saurabh/programming/python_file/chess_game/chess/images/white_pawn.png")
w_queen = pygame.image.load("/home/saurabh/programming/python_file/chess_game/chess/images/white_queen.png")
w_rook = pygame.image.load("/home/saurabh/programming/python_file/chess_game/chess/images/white_rook.png")