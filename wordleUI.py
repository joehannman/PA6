import random
from wordleLL import WordleLL
from UIutils.Ui_utils import Screen
from UIutils.Ui_utils import SPACING
from UIutils.Ui_utils import LOGO

class Wordle:
    def __init__(self, user=None) -> None:
        self.logic_layer = WordleLL()
        # Generate Word bank
        self.word_bank = self.logic_layer.get_word_bank()
        self.word = None

        self.user = user
        self.prev_words = None
        self.score = 0
        self.word_length = 0
        self.won = False

        # Alphabet
        self.a = None
        
        self.wins = 0
        self.losses = 0
        self.streak = 0
        self.games_played = 0
        self.cur_round = 0
        self.rounds = 6

        self.screen = Screen()



    def initalize_game(self, length):
        self.won = False
        # Reseting the Alphabet
        self.a = {"A": "A", 
                  "B": "B", 
                  "C": "C", 
                  "D": "D", 
                  "E": "E",
                  "F": "F", 
                  "G": "G", 
                  "H": "H", 
                  "I": "I", 
                  "J": "J",
                  "K": "K", 
                  "L": "L", 
                  "M": "M", 
                  "N": "N", 
                  "O": "O",
                  "P": "P", 
                  "Q": "Q", 
                  "R": "R", 
                  "S": "S", 
                  "T": "T",
                  "U": "U", 
                  "V": "V", 
                  "W": "W", 
                  "X": "X", 
                  "Y": "Y",
                  "Z": "Z"}
        self.cur_round = 0
        self.prev_words = [""] * self.rounds
        self.word = self.logic_layer.get_word(self.word_bank, length).lower()
        self.word_length = len(self.word)

    def get_stats(self) -> str:
        """
        Returns a string of current win, round and streak stats
        """
        wins = f"Wins: {self.wins} / {self.games_played}"
        rounds = f"Round: {min(self.cur_round+1, self.rounds)} / {self.rounds}"
        rounds_len = len(rounds)
        streak = f"Streak: \033[3{self.streak%8}m{self.streak}\033[0m"
        score = f"Score: {self.score}"

        header = f"  {wins}   {rounds}   {streak}\n"
        header += f"╘{'═'*(len(wins)+2)}╧{'═'*(rounds_len//2)}{'─'*(rounds_len-(rounds_len//2)+2)}┴─────────····· ·  ·"

        return header

    def get_keyboard(self):
        """
        Returns the keyboard in the eng keyboard layout as a string
        """
        return f"""{SPACING}{self.a["Q"]} {self.a["W"]} {self.a["E"]} {self.a["R"]} {self.a["T"]} {self.a["Y"]} {self.a["U"]} {self.a["I"]} {self.a["O"]} {self.a["P"]}
{SPACING} {self.a["A"]} {self.a["S"]} {self.a["D"]} {self.a["F"]} {self.a["G"]} {self.a["H"]} {self.a["J"]} {self.a["K"]} {self.a["L"]}
{SPACING}  {self.a["Z"]} {self.a["X"]} {self.a["C"]} {self.a["V"]} {self.a["B"]} {self.a["N"]} {self.a["M"]}"""


    def print_guesses(self, lost=False):
        self.screen.clear_screen()

        # Header
        print(self.get_stats())

        # Logo
        print(LOGO)
        
        # Printing each guessed word with fancy boarder
        print(f"{SPACING} ╔══───··")
        for i, word in enumerate(self.prev_words):
            print(f"{SPACING} ║ {i + 1}. {word}")
        print(f"{SPACING} ╚══╗", end="")

        # Print the solution in red if game is lost
        if lost: print(f" \033[31m{' '.join(self.word.upper())}\033[0m", end="")
        print(f"\n{SPACING}    ╚══───···")
    
        # Keyboard visualization
        print(self.get_keyboard())
        print(self.word)
        print()



    def prompt_guess(self):
        self.print_guesses()
        guess = input("Make a guess: ").lower()
        while not self.logic_layer.validate_guess(guess, self.word):
            self.print_guesses()
            guess = input(f"\033[31m{guess.upper()}\033[0m is not valid. \nMake a guess: ").lower()
        self.screen.clear_screen()
        print()


        ret_str = ""
        for i in range(len(guess)):
            if guess[i] == self.word[i]:
                ret_str += f"\033[32m{guess[i].upper()}\033[0m "

                # Coloring the keyboard letters green
                self.a[guess[i].upper()] = f"\033[32m{guess[i].upper()}\033[0m"

            elif guess[i] in self.word:
                ret_str += f"\033[33m{guess[i].upper()}\033[0m "

                # Coloring a letter yellow, but not if a letter is already green
                if self.a[guess[i].upper()] != f"\033[32m{guess[i].upper()}\033[0m":
                    self.a[guess[i].upper()] = f"\033[33m{guess[i].upper()}\033[0m"

            else:
                ret_str += f"\033[30m{guess[i].upper()}\033[0m "
                
                # Coloring the keyboard letters black
                self.a[guess[i].upper()] = f"\033[30m{guess[i].upper()}\033[0m"

        self.prev_words[self.cur_round] = ret_str
        self.cur_round+=1

        return guess

        

    def check_guess(self, guess):
        if self.logic_layer.validate_guess(guess, self.word):        
            self.prev_words[self.cur_round] = guess
            ret_string = ""
            
            for i in range(len(guess)):
                if self.word[i].lower() == guess[i].lower():
                    ret_string += guess[i].upper() + " "
                    continue

                if guess[i] in self.word:
                    ret_string += guess[i].lower() + " "
                    continue

                ret_string += "_ "

            self.won = self.logic_layer.check_for_win(guess, self.word)
                
            return ret_string + "\n"
        

    def play(self):
        self.screen.clear_screen()
        print(LOGO)
        user_input = input(f"Choose word length: ")
        while not self.logic_layer.validate_word_length(user_input):
            self.screen.clear_screen()
            print(LOGO)
            print("Invalid length, word length must range between 3 and 10 letters")
            user_input = input(f"Choose word length: ")

        self.initalize_game(user_input)
        self.guesses = 5
        
        while self.guesses >= 0:
            guess = self.prompt_guess()
            print(guess)
            self.guesses -=  1
            if self.logic_layer.check_for_win(guess, self.word):
                self.print_guesses()
                # print(self.prev_words[self.cur_round-1])
                print("\nYou win!")
                self.wins += 1
                self.streak += 1
                self.games_played += 1
                self.score += self.guesses
                return

        self.print_guesses(True) 
        print("You lose")
        self.losses += 1
        self.streak = 0
        self.score = 0
        self.games_played += 1
