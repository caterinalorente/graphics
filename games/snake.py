import pygame, sys
from pygame.locals import *
import random, time, sys
from numpy import zeros

class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col

def initial_position():
    col = random.randint(0,10)
    row = random.randint(0,10)
    position = Position(5, 5)
    #return [row,col]
    return(position)
        
def clean_matrix(matrix, pos):
    matrix[pos.row][pos.col] = 0
            
def move_snake(matrix, pos, dir):
    clean_matrix(matrix, pos)
    pos.row += dir[0]
    pos.col += dir[1]
    matrix[pos.row][pos.col] = 1

def zero():
    # Create zero matrix
    matrix = zeros([10,10], int)  
    return matrix

def show(matrix):
    for row in range(0, 10):
        line = []
        for col in range(0, 10):
            line.append(matrix[row][col])
        print line
    print "\n"        
            
def main():
    a = zero()
    dir = [0,0]
    position = initial_position()
    for i in range(0, 10):
        move_snake(a, position, dir)
        show(a)
        key = raw_input("")
        if key == "a": 
            dir[0] = 0
            dir[1] = -1
        elif key == "d": 
            dir[0] = 0
            dir[1] = 1
        elif key == "w": 
            dir[0] = -1
            dir[1] = 0
        elif key == "x": 
            dir[0] = 1
            dir[1] = 0

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Snake')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()