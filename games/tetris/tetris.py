import random, time, os

def choose_tetromino():
    tetrominos = {'I':[[0,0,0],[1,1,1],[0,0,0]],
                  'L':[[1,0,0],[1,0,0],[1,1,0]],
                  'J':[[0,0,1],[0,0,1],[0,1,1]],
                  'S':[[0,1,1],[1,1,0],[0,0,0]],
                  'Z':[[1,1,0],[0,1,1],[0,0,0]],
                  'T':[[1,1,1],[0,1,0],[0,0,0]],
                  'O':[[1,1,0],[1,1,0],[0,0,0]]}
    
    selected = random.choice(['I','L','J','S','Z','T','O'])
    print selected
    return tetrominos[selected]

def position_tetromino():
    col = random.randint(0,7)
    return col

def place_tetromino(matrix, tetromino, row, col):
    for i in range(0, 3):
        for j in range(0, 3):
#            matrix[i+row][j+col] = tetromino[i][j]
            matrix[i+row][j+col] = 1
    return(matrix)
            
def clean_tetromino(matrix, row, col):
    for i in range(0, 3):
        for j in range(0, 3):
            if matrix[i+row][j+col] == 1: matrix[i+row][j+col] = 0
    return(matrix)
            
def move_down_tetromino(matrix, tetromino, row, col):
    cleanedMatrix = clean_tetromino(matrix, row, col) 
    return(place_tetromino(cleanedMatrix, tetromino, row+1, col))
    
    
def zero():
    # Create zero matrix
    matrix = [[0] * 10] *10
    return matrix

def show(matrix):
    for col in matrix: print col
    
def main():
    a = zero()
    tetromino = choose_tetromino()
    a = place_tetromino(a, tetromino, 0, 3)
    show(a)
    for i in range(0, 10):
        a = move_down_tetromino(a, tetromino, 0, 3)
        show(a)
        print ""
        time.sleep(1)
main()