from wordleLL import WordleLL
from UIutils.Ui_utils import Screen
from UIutils.Ui_utils import SPACING
from UIutils.Ui_utils import LOGO
from wordleUI import Wordle

class PlayMenu:
    def __init__(self, user, user_id) -> None:
        self.logic_layer = WordleLL()
        self.screen = Screen()
        self.user = user
        self.user_id = user_id

    def menu_output(self) -> None:
        self.screen.clear_screen()
        print(LOGO)
        print(f"{SPACING}··─ {self.user} ─··")
        print()
        print(f"{SPACING}(P)lay")
        print(f"{SPACING}(H)ighscore")
        print()
        print(f"{SPACING}(B)ack")

    def input_prompt(self):
        self.menu_output()
        user_input = input(" ")
        if user_input.lower() == "b":
            return
        if user_input.lower() == "p":
            wordle = Wordle()
            while True:
                wordle.play()
                print(f"\nWins: {wordle.wins}, Losses: {wordle.losses}\nCurrent streak: {wordle.streak}\nCurrent score: {wordle.score}\n")
                play_again = input("Press any key to play again or (q)uit: ")
                if play_again.lower() == "q": break