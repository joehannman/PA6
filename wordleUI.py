import random
import os
from wordleLL import WordleLL
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def header():
    print("█░█░█ █▀█ █▀█ █▀▄ █░░ █▀▀   █▀▀ ▄▀█ █▀▄▀█ █ █▄░█ █▀▀")
    print("▀▄▀▄▀ █▄█ █▀▄ █▄▀ █▄▄ ██▄   █▄█ █▀█ █░▀░█ █ █░▀█ █▄█")
class Wordle:
    def __init__(self, user=None, length= 5) -> None:
        self.logic_wrapper = WordleLL()
        self.user = user
        self.word = None
        self.word_bank = None
        self.wins = 0
        self.losses = 0
        self.streak = 0
        self.games_played = 0
        self.prev_words = []
        self.score = 0
        self.word_length = length
        self.won = False

    def initalize_word(self):
        self.won = False
        self.prev_words = []
        self.word = self.logic_wrapper.get_word()

    def prompt_guess(self):
        if self.prev_words:
            print("Previously guessed words:")
            print()
            for word in self.prev_words:
                print(word)
            print()

        guess = input("Make a guess: ").lower()
        clear_screen()
        header()
        print()
        print(self.word)

        return self.check_guess(guess)

    def check_guess(self, guess):
        if len(guess) > self.word_length:
            return f"Guess cannot exceed {self.word_length} letters"
              
        self.prev_words.append(guess)
        ret_string = ""
        
        for i in range(len(guess)):
            if self.word[i].lower() == guess[i].lower():
                ret_string += guess[i].upper() + " "
                continue

            if guess[i] in self.word:
                ret_string += guess[i].lower() + " "
                continue

            ret_string += "_ "

        if guess.lower() == self.word.lower(): self.won = True
            
        return ret_string + "\n"

    def play(self):
        clear_screen()
        header()
        self.initalize_word()
        self.guesses = 5
        
        while self.guesses >= 0:
            guess = self.prompt_guess()
            print(guess)
            print(f"{self.guesses} guesses left.")
            self.guesses -=  1
            if self.won:
                print("\nYou win!")
                self.wins += 1
                self.streak += 1
                self.games_played += 1
                self.score += self.guesses
                return
            
        print("You lose")
        self.losses += 1
        self.streak = 0
        self.score = 0
        self.games_played += 1
