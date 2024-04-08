from screen import Screen
import random

SPACING = "\t\t"

# Debug
SHOW_WORD = False
USE_TEST_WORD = False
TEST_WORD = "brain"


class Alphabet:
    def __init__(self, language="english") -> None:
        self.english = {"A": "A", 
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
        self.icelandic = {"A": "A",
                            "Á": "Á",
                            "B": "B", 
                            "C": "C", 
                            "D": "D",
                            "Ð": "Ð", 
                            "E": "E",
                            "É": "É",
                            "F": "F", 
                            "G": "G", 
                            "H": "H", 
                            "I": "I",
                            "Í": "Í", 
                            "J": "J",
                            "K": "K", 
                            "L": "L", 
                            "M": "M", 
                            "N": "N", 
                            "O": "O",
                            "Ó": "Ó",
                            "P": "P", 
                            "Q": "Q", 
                            "R": "R", 
                            "S": "S", 
                            "T": "T",
                            "U": "U", 
                            "Ú": "Ú",
                            "V": "V", 
                            "W": "W", 
                            "X": "X", 
                            "Y": "Y",
                            "Ý": "Ý",
                            "Z": "Z",
                            "Þ": "Þ"}
        self.language = language
        language_dict = {"english": self.english, "icelandic": self.icelandic}
        self.a = language_dict[self.language]

    def set_green(self, letter):
        self.a[letter.upper()] = f"\033[32m{letter.upper()}\033[0m"

    def set_yellow(self, letter):
        if self.a[letter.upper()] != f"\033[32m{letter.upper()}\033[0m":
            self.a[letter.upper()] = f"\033[33m{letter.upper()}\033[0m"

    def set_black(self, letter):
        self.a[letter.upper()] = f"\033[30m{letter.upper()}\033[0m"
            
    def get_keyboard(self):
        eng_kbd = f"""{SPACING}{self.a["Q"]} {self.a["W"]} {self.a["E"]} {self.a["R"]} {self.a["T"]} {self.a["Y"]} {self.a["U"]} {self.a["I"]} {self.a["O"]} {self.a["P"]}
{SPACING} {self.a["A"]} {self.a["S"]} {self.a["D"]} {self.a["F"]} {self.a["G"]} {self.a["H"]} {self.a["J"]} {self.a["K"]} {self.a["L"]}
{SPACING}  {self.a["Z"]} {self.a["X"]} {self.a["C"]} {self.a["V"]} {self.a["B"]} {self.a["N"]} {self.a["M"]}"""
        ice_kbd = f"""{SPACING}{self.a["Q"]} {self.a["W"]} {self.a["E"]} {self.a["É"]} {self.a["R"]} {self.a["T"]} {self.a["Y"]} {self.a["Ý"]} {self.a["U"]} {self.a["Ú"]} {self.a["I"]} {self.a["Í"]} {self.a["O"]} {self.a["Ó"]} {self.a["P"]} {self.a["Ð"]}
{SPACING} {self.a["A"]} {self.a["Á"]} {self.a["S"]} {self.a["D"]} {self.a["F"]} {self.a["G"]} {self.a["H"]} {self.a["J"]} {self.a["K"]} {self.a["L"]}
{SPACING}  {self.a["Z"]} {self.a["X"]} {self.a["C"]} {self.a["V"]} {self.a["B"]} {self.a["N"]} {self.a["M"]}  {self.a["Þ"]}"""
        keyboards = {"english": eng_kbd, "icelandic": ice_kbd}

        return keyboards[self.language]
        
    def is_in_alphabet(self, letter):
        return True if letter in self.a else False

class Wordle:
    def __init__(self, no_rounds=6, letter_length=5) -> None:
        self.user = None
        self.word = None
        self.word_bank = None
        self.letter_length = letter_length
        # Alphabet
        self.a = None

        # How many rounds will be played
        self.rounds = no_rounds
        # The current round
        self.cur_round_index = 0
        # Each guess
        self.guessed_words = None

        self.games_played = 0
        self.wins = 0
        self.streak = 0
        self.score = 0
        
        self.screen = Screen()

    def _get_keyboard(self):
        return f"""{SPACING}{self.a["Q"]} {self.a["W"]} {self.a["E"]} {self.a["R"]} {self.a["T"]} {self.a["Y"]} {self.a["U"]} {self.a["I"]} {self.a["O"]} {self.a["P"]}
{SPACING} {self.a["A"]} {self.a["S"]} {self.a["D"]} {self.a["F"]} {self.a["G"]} {self.a["H"]} {self.a["J"]} {self.a["K"]} {self.a["L"]}
{SPACING}  {self.a["Z"]} {self.a["X"]} {self.a["C"]} {self.a["V"]} {self.a["B"]} {self.a["N"]} {self.a["M"]}"""


    def _initalize_game(self) -> None:
        """
        Initializes word to a random word from file, and resets variables
        """
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
        self.cur_round_index = 0
        self.guessed_words = [""] * self.rounds
        with open(f"word_bank_{self.letter_length}.txt") as fo:
            self.word = random.choice(fo.readlines()).strip()
        
        # DEBUG
        if USE_TEST_WORD:
            self.word = TEST_WORD


    def _print_guesses(self, lost=False) -> None:
        """
        Prints all previous guesses along with the stats header and keyboard
        """
        self.screen.clear_screen()

        # Header
        print(self._get_stats())

        # Logo
        print(f"""{SPACING}╦ ╦╔═╗╦═╗╔╦╗╦  ╔═
{SPACING}╙╨╜╙─╜╨╙─ ╨╜╨─╜╙─""")
        
        # Printing each guessed word with fancy boarder
        print(f"{SPACING} ╔══───··")
        for i, word in enumerate(self.guessed_words):
            print(f"{SPACING} ║ {i + 1}. {word}")
        print(f"{SPACING} ╚══╗", end="")

        # Print the solution in red if game is lost
        if lost: print(f" \033[31m{' '.join(self.word.upper())}\033[0m", end="")
        print(f"\n{SPACING}    ╚══───···")
    
        # Keyboard visualization
        print(self._get_keyboard())
        print()

        # DEBUG
        if SHOW_WORD:
            print(f"DEBUG: {self.word}")


    def _get_stats(self) -> str:
        """
        Returns a string of current win, round and streak stats
        """
        wins = f"Wins: {self.wins} / {self.games_played}"
        rounds = f"Round: {min(self.cur_round_index+1, self.rounds)} / {self.rounds}"
        rounds_len = len(rounds)
        streak = f"Streak: \033[3{self.streak%8}m{self.streak}\033[0m"

        header = f"  {wins}   {rounds}   {streak}\n"
        header += f"╘{'═'*(len(wins)+2)}╧{'═'*(rounds_len//2)}{'─'*(rounds_len-(rounds_len//2)+2)}┴─────────····· ·  ·"

        return header


    def _prompt_guess(self) -> str:
        """
        Prints out previous guesses and asks user to make a guess
        """
        self._print_guesses()
        guess = input("Make a guess: ").lower()
        while not self._check_validity(guess):
            self._print_guesses()
            guess = input(f"\033[31m{guess.upper()}\033[0m is not valid. \nMake a guess: ").lower()
        
        return guess


    def _check_validity(self, guess:str) -> bool:
        """
        Checks validity of a word, perhaps more constraints will be added
        """
        if len(guess) == self.letter_length:
            return True
        return False


    def _compare_guess(self, guess:str) -> str:
        """
        Compares the guessed word with the answer
        """
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

        self.guessed_words[self.cur_round_index] = ret_str
        self.cur_round_index+=1

        return ret_str


    def play(self) -> None:
        """
        Main gameplay loop
        """
        while True:
            self._initalize_game()
            for _ in range(self.rounds):
                guess = self._prompt_guess()
                self._compare_guess(guess)
                if guess == self.word:
                    lost = False
                    self.wins += 1
                    self.streak += 1
                    break
            else:
                lost = True
                self.streak = 0

            self.games_played += 1
            self._print_guesses(lost)

            if input(f"Play again y/n: ").lower() == "n":
                return

    
w = Wordle()
w.play()