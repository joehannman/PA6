from logic.wordleLL import WordleLL
from UIutils.Ui_utils import Screen
from UIutils.Ui_utils import SPACING
from UIutils.Ui_utils import LOGO

class HighScoreMenu:
    def __init__(self, user="gudni", user_id=0) -> None:
        self.logic_layer = WordleLL()
        self.screen = Screen()
        self.user = user
        self.user_id = user_id

    def menu_output(self) -> None:
        score_list = self.logic_layer.get_scores()
        player_score_list = self.logic_layer.get_scores_by_player(self.user)
        self.screen.clear_screen()
        print(LOGO)
        print(f"{SPACING}··─ {self.user} ─··")
        print()
        print(f"{SPACING}Hi score")
        print()
        print(f"\tPersonal Best   ║ All time Best")
        print("\t════════════════╬════════════════════")
        for i in range(10):
            prt_str = ""
            if i < len(player_score_list): prt_str += f"\t{i+1}. {player_score_list[i][1]}{SPACING}║"
            else:
                prt_str += f"\t{i+1}{SPACING}║"
            if i < len(score_list): prt_str += f" {i+1}. {score_list[i][0]}: {score_list[i][1]}"
            else:
                prt_str += f" {i+1}"

            print(prt_str)
        print("\t════════════════╩════════════════════")

        

    def input_prompt(self):
        self.menu_output()
        user_input = input("Press [ENTER] to go back: ")
        if user_input.lower() == "b":
            return
        
if __name__ == "__main__":
    hs = HighScoreMenu()
    hs.menu_output()