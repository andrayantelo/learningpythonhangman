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
            time.sleep(0.01)   # Or whatever delay you'd like
        print   # One last print to make sure that you move to a new line
        
    def clear_screen(self):
    #clear screen variable (how many blank lines to print)
        print "\n"* self.SCREEN_SIZE
        
    def scene(self):
        pass

        
        
def run_game():
    pass
    

mygame = Hangman()

intro_text = textwrap.dedent("""
The year is 1750. You are a resident of England and have been charged with a crime! 
You attempted to steal an apple at the market. You have been scheduled to be hanged 
in the village of Tyburn UNLESS you can guess the secret word that is chosen by the
king. 
""")

cool_print(intro_text)

raw_input("Press ENTER to Continue.\n> ")

print intro_text
clear_screen()
print king
time.sleep(1)
clear_screen()
print king_speaks
time.sleep(1)
clear_screen()
print king
time.sleep(1)
clear_screen()

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

