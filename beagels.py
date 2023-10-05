import numbers
import random

NUM_DIGITS=2
MAX_GUESS = 10

def main():
    print(f'''Bagels, a deductive logic game.
            By Al Sweigart al@inventwithpython.com
        
                I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
            Try to guess what it is. Here are some clues:
            When I say:
            That means:
                Pico    One digit is correct but in the wrong position.
                Fermi   One digit is correct and in the right position.
                Bagels  No digit is correct.
                For example, if the secret number was 248 and your guess was 843, the
            clues would be Fermi Pico.''')
    
    while True:
        secretNum = getSecretNum()
        print('I have thought of a number')
        print(f'You have {MAX_GUESS} tries to get it')

        numGuesses = 1
        while numGuesses <= MAX_GUESS:
            guess = ''
            # Keep Looping untill the num is right
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Gues #{numGuesses}:')
                guess = input('> ')
                
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses +=1

            if guess == secretNum:
                break #they're correct, so brak the loop
            if numGuesses > MAX_GUESS:
                print('You ran out of guesses')
                print(f'the answear was {secretNum}.')

        #ask a player if they wanna play again
        print('Do You Want to play again?')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for Playing')

def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789') # a list of numbers
    random.shuffle(numbers) #shuffle numbers into random order

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNumb = ''
    for i in range(NUM_DIGITS):
        secretNumb +=str(numbers[i])
    return secretNumb

def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""
    if guess == secretNum:
        return 'You got it'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # A correct digit is in the incorrect place.
            clues.append('Pico')
    
    if len(clues) == 0:
        return 'Beagels'    # There are no correct digits at all.
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return ' '.join(clues)
    
# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
