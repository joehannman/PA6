from wordleLL import WordleLL
from UIutils.Ui_utils import Screen
from UIutils.Ui_utils import SPACING
from UIutils.Ui_utils import LOGO

class HighScoreMenu:
    def __init__(self, user="gudni", user_id=0) -> None:
        self.logic_layer = WordleLL()
        self.screen = Screen()
        self.user = user
        self.user_id = user_id
        self.player_scores = self.logic_layer.get_player_scores()[self.user]

    def menu_output(self) -> None:
        score_list = self.logic_layer.get_scores()
        player_score_list = self.logic_layer.get_scores_by_player(self.user)
        self.screen.clear_screen()
        print(player_score_list)
        input()
        print(LOGO)
        print(f"{SPACING}··─ {self.user} ─··")
        print()
        print(f"{SPACING}Hi score")
        for i in range(len(score_list)):
            print(f"{i+1}. {score_list[i][1]}, {score_list[i][0]}")
        print(self.player_scores)

    def input_prompt(self):
        self.menu_output()
        user_input = input("")
        if user_input.lower() == "b":
            return
        
if __name__ == "__main__":
    hs = HighScoreMenu()
    hs.menu_output()