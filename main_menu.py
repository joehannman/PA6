from wordleLL import WordleLL
from play_menu import PlayMenu
from UIutils.Ui_utils import Screen
from UIutils.Ui_utils import SPACING
from UIutils.Ui_utils import LOGO


class MainMenuUI:
    def __init__(self) -> None:
        self.logic_layer = WordleLL()
        self.screen = Screen()
        self.users = self.logic_layer.get_all_users()

    def menu_output(self) -> None:
        self.screen.clear_screen()
        print(LOGO)
        print()
        self.list_all_users()
        print()

    def list_all_users(self):
        self.users
        for (key, value) in self.users.items():
            print(f"{SPACING}{key}. {value}")

    def input_prompt(self) -> None:
        user_input = ""
        while user_input != "q":
                self.menu_output()
                user_input = input("Select user index or (c)reate new User: ").lower()
                if user_input.lower() == "c":
                    self.prompt_new_user()
                else:
                    # indexing into the user dictionary 
                    if user_input in self.users:
                        user = self.users[user_input]
                        play_menu = PlayMenu(user) 
                        play_menu.input_prompt()

        print("\nQUITTING")

    def prompt_new_user(self):
        self.screen.clear_screen()
        print(LOGO)
        print()
        new_user = input("Please enter desired username: ")
        self.logic_layer.save_new_user(new_user)
        self.user = new_user


mm = MainMenuUI()
mm.input_prompt()