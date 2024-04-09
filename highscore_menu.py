from wordleLL import WordleLL
from UIutils.Ui_utils import Screen
from UIutils.Ui_utils import SPACING
from UIutils.Ui_utils import LOGO

class HighScoreMenu:
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
        print(f"{SPACING}Hi score")


    def input_prompt(self):
        self.menu_output()
        user_input = input("")
        if user_input.lower() == "b":
            return
