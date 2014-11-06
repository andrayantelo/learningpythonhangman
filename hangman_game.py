import random

HANGMAN_ALREADYGUESSED = 'ALREADY_GUESSED'
HANGMAN_CONTINUE = 'HANGMAN_CONTINUE'
HANGMAN_ONELETTER = 'HANGMAN_ONELETTER'
HANGMAN_ALPHABET = 'HANGMAN_ALPHABET'
HANGMAN_HEAD = 'HANGMAN_HEAD'
HANGMAN_ONEARM = 'HANGMAN_ONEARM'
HANGMAN_TWOARMS = 'HANGMAN_TWOARMS'
HANGMAN_UPPER = 'HANGMAN_UPPER'
HANGMAN_LOWER = 'HANGMAN_LOWER'
HANGMAN_ONELEG = 'HANGMAN_ONELEG'
HANGMAN_LOSE = 'HANGMAN_LOSE'
HANGMAN_WIN = 'HANGMAN_WIN'

class Hangman(object):
	
    def __init__(self, screen_size = 100):
        self.screen_size = screen_size
        self.allowed_letters = 'abcdefghijklmnopqrstuvwxyz'
        self.wordlist = 'Apple Watermelon Pineapple Papaya Strawberry Blueberry Fig Durian'.split()
        self.list_of_words = "words.txt"
        self.secret_word = 'apple'
        self.guess = ''
        self.guesses = []
        self.trimmed_incorrect_guesses =[]
        self.incorrect_guesses = []
        self.correct_guesses = []

    def choose_random_word(self):
         self.secret_word = random.choice(self.wordlist)   
         return self.secret_word
        
    def construct_billboard(self):
        
        self.billboard = list(self.secret_word)
        for i, letter in enumerate(self.billboard):
            if letter not in self.guesses:
                self.billboard[i] = "_"
        return ' '.join(self.billboard)
        
    def validate_guess(self, letter):
        if len(letter) != 1:
            return HANGMAN_ONELETTER
        elif letter in self.guesses:
            return HANGMAN_ALREADYGUESSED
        elif letter not in self.allowed_letters:
            return HANGMAN_ALPHABET
        self.guesses.append(letter)
        
        
    def guess_status(self):
        for letter in self.guesses:
            if letter not in self.secret_word:
                self.incorrect_guesses.append(letter)
    
            elif letter in self.secret_word:
                self.correct_guesses.append(letter)
       
    def game_status(self):
        guesses = self.guesses
        for letter in self.incorrect_guesses:
            if letter not in self.trimmed_incorrect_guesses:
                self.trimmed_incorrect_guesses.append(letter)
        missed = self.trimmed_incorrect_guesses
        hit = set(self.correct_guesses)
        if len(missed) == 1:
            return HANGMAN_HEAD
        elif len(missed) == 2:
            return HANGMAN_ONEARM
        elif len(missed) == 3:
            return HANGMAN_TWOARMS
        elif len(missed) == 4:
            return HANGMAN_UPPER
        elif len(missed) == 5:
            return HANGMAN_LOWER
        elif len(missed) == 6:
            return HANGMAN_ONELEG
        elif len(missed) >= 7:
            return HANGMAN_LOSE
        elif hit >= set(self.secret_word):
            return HANGMAN_WIN
        else:
            return HANGMAN_CONTINUE
