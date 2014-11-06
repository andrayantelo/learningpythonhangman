# This is the hangman game.
import sys
from hangmanascii import *
import time
import string
import textwrap
from hangman_game import *

#list_of_words = "words.txt"

class RenderGame(object):
    
    def __init__(self):
        self.SCREEN_SIZE = 100
    

    def load_wordlist(self):
        alphabet = set('abcdefghijklmnopqrstuvwxyz')
        self.lines = open(self.list_of_words).read().decode('utf-8').split('\n')
        self.lines = [line for line in self.lines if line.isalpha()]
        self.lines = [line for line in self.lines if line.islower()]
        self.lines = [line for line in self.lines if len(line) > 6]
        self.lines = [line for line in self.lines if set(line) <= alphabet]
   
        #print self.lines
        return self.lines
        

        
    def cool_print(self, str):
        textwrap.dedent(str)
        for char in str:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)   
        print   
        
    def clear_screen(self):
        print "\n"* self.SCREEN_SIZE
        
    def scene(self):
        pass

        
        
def run_game():
    pass
    

mygame = Hangman()



while True:

    mygame.guess = raw_input("Guess a letter!\n> ")


    result = mygame.validate_guess(mygame.guess)


    if result == HANGMAN_ONELETTER:
        print "Please type one letter."
    
    elif result == HANGMAN_ALREADYGUESSED:
        print "You already guessed that letter."
    
    elif result == HANGMAN_ALPHABET:
        print "Please type a letter from the English alphabet."

    
    mygame.construct_billboard()
    print mygame.construct_billboard()
    mygame.guess_status()
    state = mygame.game_status()
    
    if state == HANGMAN_LOSE:
        print "Quit?"
        break
    
    elif state == HANGMAN_WIN:
        print "Congratulations"
        break
        
    elif state == HANGMAN_CONTINUE:
        pass
        
    print mygame.trimmed_incorrect_guesses

