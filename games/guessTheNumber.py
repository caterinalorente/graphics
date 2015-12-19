import random

MAX_GUESSES = 6

def number_range():
    min, max = [0, 100]
    a = random.randint(min, max)
    b = random.randint(min, max)
    while a == b: b = random.randint(min, max)
    if a > b: return(b,a)
    else: return(a,b)
    
def get_number_to_guess(min, max):
    numberToGuess = random.randint(min,max)
    return(numberToGuess)
    
def check_guess(numberToGuess):
    attempts = 0
    while  (attempts < MAX_GUESSES):
        guess = int(raw_input("Take a guess: "))
        attempts += 1
        
        if guess > numberToGuess:   print "Your guess is too high."
        elif guess < numberToGuess: print "Your guess is too low."
        else: return(attempts, True)
        
    return(attempts, False)  

def main():
    name = raw_input("Hello! What is your name? ")
    
    min, max = number_range()
    print "Well, %s, I am thinking of a number between %s and %s" %(name, min, max)
    
    numberToGuess = get_number_to_guess(min,max)
    attempts, guessResult = check_guess(numberToGuess)
    if guessResult == True:
        print "Good job, %s! You guessed my number in %s guesses!" %(name, attempts)
    else:
        print "You exceeded the maximum number of attempts (%s). The number was %s" %(MAX_GUESSES, numberToGuess)
    
main()