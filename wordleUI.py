import random
import os
from wordleLL import WordleLL
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def header():
    print("█░█░█ █▀█ █▀█ █▀▄ █░░ █▀▀   █▀▀ ▄▀█ █▀▄▀█ █ █▄░█ █▀▀")
    print("▀▄▀▄▀ █▄█ █▀▄ █▄▀ █▄▄ ██▄   █▄█ █▀█ █░▀░█ █ █░▀█ █▄█")
class Wordle:
    def __init__(self, user=None) -> None:
        self.logic_wrapper = WordleLL()
        self.user = user
        self.word = None
        self.word_bank = self.logic_wrapper.get_word_bank()
        self.wins = 0
        self.losses = 0
        self.streak = 0
        self.games_played = 0
        self.prev_words = []
        self.score = 0
        self.word_length = 0
        self.won = False

    def initalize_word(self, length):
        self.won = False
        self.prev_words = []
        self.word = self.logic_wrapper.get_word(self.word_bank, length)
        self.word_length = len(self.word)

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
        if self.logic_wrapper.validate_guess(guess, self.word):        
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

            self.won = self.logic_wrapper.check_for_win(guess, self.word)
                
            return ret_string + "\n"

    def play(self):
        clear_screen()
        header()
        user_input = int(input(f"Choose word length: "))
        self.initalize_word(user_input)
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
