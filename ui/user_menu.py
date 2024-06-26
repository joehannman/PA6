from logic.wordleLL import WordleLL
from UIutils.Ui_utils import Screen
from UIutils.Ui_utils import SPACING
from UIutils.Ui_utils import LOGO
from ui.wordleUI import Wordle
from ui.highscore_menu import HighScoreMenu


class UserMenu:
    def __init__(self, user, user_id, word_bank) -> None:
        self.word_bank = word_bank
        self.logic_layer = WordleLL()
        self.screen = Screen()
        self.user = user
        self.user_id = user_id

    def menu_output(self) -> None:
        self.screen.clear_screen()
        print(LOGO)
        print(f"{SPACING}··─ {self.user} ─··")
        print()
        print(f"{SPACING}[P]lay")
        print(f"{SPACING}[H]ighscore")
        print()
        print(f"{SPACING}[B]ack")

    def input_prompt(self):
        while True:
            self.menu_output()
            user_input = input("\nSelect option: ")

            if user_input.lower() == "b":
                return
            
            if user_input.lower() == "p":
                self.invoke_game()

            if user_input.lower() == "h":
                self.invoke_highscore()

    def invoke_game(self):
        wordle = Wordle(self.word_bank)
        while True:
            wordle.play()
            play_again = input("Press any key to play again or (q)uit: ")
            if play_again.lower() == "q": 
                if wordle.score > 0:
                    self.logic_layer.save_score(self.user, wordle.score)
                break

    def invoke_highscore(self):
        high_score_menu = HighScoreMenu(self.user)
        high_score_menu.input_prompt()