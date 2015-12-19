import random 

pictures = ['''
H A N G M A N
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def get_word_to_guess():
    arrayOfPossibleWords = "Sheldom Lennart Rajesh Wolowitz".split()
    min = 0
    max = len(arrayOfPossibleWords)-1
    index = random.randint(min, max)
    return(arrayOfPossibleWords[index])

def transform_word_into_set(word):
    word = word.lower()
    s = set(word)      
    return(s)

def print_state(word, setToGuess):
    status = []
    for i in range(0, len(word)):
        if word[i].lower() in setToGuess: status.append("_ ")
        else:   status.append(word[i]) 
    print ''.join(status)  
    print ''

def guess_a_letter(word, setToGuess, lettersTried, errors):
    guess = raw_input("Guess a letter: ")
    
    if guess.isdigit() != True:         # check input is a letter     
        guess = guess.lower()           # python sees h and H as different
        
        if guess not in lettersTried:   # user didn't try this letter 
            lettersTried.append(guess) 
            if guess in setToGuess:
                setToGuess.remove(guess)
                if len(setToGuess) == 0: return(errors, True)
            else:
                print "Wrong letter"
                errors += 1
                
        else: 
            print "You already guessed letter %s \nSo far you've tried %s" %(guess, lettersTried)
                        
    else:
        print ("Hey, you didn't enter a letter. Behave! \nGuess a LETTER: ")

    return(errors, False)

def main():
    wordToGuess = get_word_to_guess()
    setToGuess = transform_word_into_set(wordToGuess)
    lettersTried = []
    errors = 0    
    win = False
    
    while win == False and errors < 7:
        print pictures[errors]
        print_state(wordToGuess, setToGuess)
        print "Letters tried so far: ", ''.join(lettersTried)
        errors, win = guess_a_letter(wordToGuess, setToGuess, lettersTried, errors)
    
    if win == False: 
        print "You didn't succeed. The hidden word was %s" %wordToGuess
    else:
        print "Bravo!! Kudos for you"

n = "y"
while n != "n":
    main()
    n = raw_input("Do you want to play again? (y/n)")
