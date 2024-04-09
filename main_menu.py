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

    def output(self) -> None:
        self.screen.clear_screen()
        print(LOGO)
        self.list_all_users()
        print(f"\n(C)reate new user{SPACING}(Q)uit")
        print()

    def list_all_users(self):
        print(f"{SPACING} ╔══───··")
        for (key, value) in self.users.items():
            print(f"{SPACING} ║ {key}. {value}")
        print(f"{SPACING} ╚═════───···")

    def input_prompt(self) -> None:
        user_input = ""
        while user_input != "q":
                self.output()
                user_input = input("Select user index: ").lower()
                if user_input.lower() == "c":
                    self.create_new_user()
                if user_input in self.users:
                    # self.invoke_play_menu()
                    user = self.users[user_input]
                    play_menu = PlayMenu(user, user_input) 
                    play_menu.input_prompt()

    def create_new_user(self):
        self.screen.clear_screen()
        print(LOGO)
        new_user = input("\n(C)ancel\nEnter desired username: ")
        if new_user.lower() == "c": return
        self.logic_layer.save_new_user(new_user)
        self.users = self.logic_layer.get_all_users()


