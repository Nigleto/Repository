import random
HANGMAN_PICS = [ '''
   +---+
       |
       |
       |
      ===''','''
   +---+
   0   |
       |
       |
      ===''','''
   +---+
   0   |
   |   |
       |
      ===''','''
   +---+
   0   |
  /|   |
       |
      ===''','''
   +---+
   0   |
  /|\  |
       |
      ===''','''
   +---+
   0   |
  /|\  |
  /    |
      ===''','''
   +---+
   0   |
  /|\  |
  / \  |
      ===''','''
   +---+
  [0   |
  /|\  |
  / \  |
      ===''','''
   +---+
  [0]  |
  /|\  |
  / \  |
      ===''']

words = {'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
         'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
         'Fruits':'apple orange lemon lime pear watermelon grape graprefruit cherry  banana cantaloupe mango strawberry tomato'.split,
         'Animals':'zebra bear ant chicken tiger spider rabbit shark snake sloth turtle wolf swan whale wombat'.split()}


def getRandomWord(wordDict):
    #this function returns a random string from the passed dictionary of lists of strings
    #first randomly select a key from the disctionary
    wordKey = random.choice(list(wordDict.keys()))

    #Second, randomly selct a word from the keys list in the dictionary
    wordIndex = random.randint(0,len(wordDict[wordKey])-1)

    return [wordDict[wordKey][wordIndex], wordKey]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # Replace blanks with correctly guessed letters.
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # Show the secret word with spcas in between each letter.
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    #  Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
    while True:
        print('Guess a letter')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')

        elif guess in alreadyGuessed:
                print('You have already guessed that letter, guess again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                print('Please enter a letter.')
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again; otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def getDifficulty():
    # This function asks the player if they want easy/medium/hard difficulty
    difficulty = 'X'
    while difficulty not in 'EMH':
        print('Enter difficulty: E - Easy, M - Medium, H - Hard')
        difficulty = input().upper()
    return difficulty



print('H A N G M A N')
enteredDifficulty = getDifficulty()
if enteredDifficulty == 'M':
        del HANGMAN_PICS[8]
        del HANGMAN_PICS[7]
if enteredDifficulty == 'H':
        del HANGMAN_PICS[8]
        del HANGMAN_PICS[7]
        del HANGMAN_PICS[5]
        del HANGMAN_PICS[3]


missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
    print('The secret word is in the set: ' + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player enter a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) -1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guessed and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    # Ask the player if they would like to play again (but only if the game is done)
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            getDifficulty()
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break
