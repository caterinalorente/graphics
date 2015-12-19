import random

def get_chip_from_user():
    chip = raw_input("Do you want to be X or O? ")
    chip = chip.lower()
    return chip

def choose_chip():
    chip = get_chip_from_user()
    
    while chip not in "xo" or len(chip) == 0:
        print("Please input X or O")
        chip = get_chip_from_user()
    
    return chip    

def who_starts_playing():
    players = ['You', 'Pc']
    return players[random.randint(0,1)]

def extract_values_from_keys(positionsUsedSoFar, chipChosen):
    for key in positionsUsedSoFar:
        chipChosen[key-1] = positionsUsedSoFar[key].upper()
    
    return chipChosen

def check_if_position_is_valid(position, positionsUsedSoFar):
    if int(position) in [1,2,3,4,5,6,7,8,9] and int(position) not in positionsUsedSoFar:
        return True
    else:
        return False 
    
def check_if_victory(position, positionsUsedSoFar):
    hor1 = [1,2,3]
    hor2 = [4,5,6]
    hor3 = [7,8,9]
    vert1 = [1,4,7]
    vert2 = [2,5,8]
    vert3 = [3,6,9]
    diag1 = [1,5,9]
    diag2 = [3,5,7]
    
    winningCombinations = {1:[hor1, vert1, diag1], 2:[hor1, vert2], 3:[hor1, vert3, diag2], \
                           4:[hor2, vert1], 5:[hor2, vert2, diag1, diag2], 6:[hor2, vert3], \
                           7:[hor3, vert1, diag2], 8:[hor3, vert2], 9:[hor3, vert3, diag1]}
    
    chip = positionsUsedSoFar[position]
    
    for line in winningCombinations[position]:
        counter = 0
        for field in line:
            if chip == positionsUsedSoFar[field]: counter += 1
            else: break
        if counter == 3: return True
        
    return False # If none of the possible combinations are True, there is no 3 in a row
    
#positionsUsedSoFar = {1:"", 2:"O", 3:"O", 4:"X", 5:"O", 6:"", 7:"X", 8:"", 9:""}      
#print check_if_victory(1, positionsUsedSoFar)
        
def print_board(positionsUsedSoFar, chipChosen):

    chipChosen = extract_values_from_keys(positionsUsedSoFar, chipChosen)    
    grid = " "*2 + chipChosen[6] + "  |" + " "*2 + chipChosen[7] + "  |" + " "*2 + chipChosen[8] + "\n" + \
    "-"*16 + "\n" + \
    " "*2 + chipChosen[3] + "  |" + " "*2 + chipChosen[4] + "  |" + " "*2 + chipChosen[5] + "\n" + \
    "-"*16 + "\n" + \
    " "*2 + chipChosen[0] + "  |" + " "*2 + chipChosen[1] + "  |" + " "*2 + chipChosen[2] + "\n"
    
    print chipChosen
    print grid
        
def game_logic(chip, player, positionsUsedSoFar):    
    
    if player == "You":
        position = raw_input("\nWhat is your move? ")
        while check_if_position_is_valid(position, positionsUsedSoFar) == False:    
            print("Please enter a position between 1 and 9 that has NOT been already taken")
            print('''
                  7 | 8 | 9
                -------------
                  4 | 5 | 6
                -------------
                  1 | 2 | 3
                ''')
            position = raw_input("\nWhat is your move? ")
            
        positionsUsedSoFar[int(position)] = chip
        nextPlayer = "Pc"
            
    elif player == "Pc":
        print "pc"
        nextPlayer = "You"
        
    print positionsUsedSoFar
    
    check_if_victory(position, positionsUsedSoFar)
    return(nextPlayer, positionsUsedSoFar, False)   

def main():
    print "Welcome to Tic Tac Toe"
#    chip = choose_chip()
#    nextPlayer = who_starts_playing()
    chip = "X"
    nextPlayer = "You"
    print "%s will start playing with chip %s" %(nextPlayer, chip.upper())
    
    positionsUsedSoFar = {}
    chipChosen=[" "]*9
    win = False
    
    while win == False:
        print_board(positionsUsedSoFar,chipChosen)
        nextPlayer, positionsUsedSoFar, win = game_logic(chip, nextPlayer, positionsUsedSoFar)    

main()