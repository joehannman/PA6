from logic.wordleLL import WordleLL
from ui.user_menu import UserMenu
from UIutils.Ui_utils import Screen
from UIutils.Ui_utils import SPACING
from UIutils.Ui_utils import LOGO


class MainMenuUI:
    def __init__(self) -> None:
        self.logic_layer = WordleLL()
        self.screen = Screen()
        self.users = self.logic_layer.get_all_users()
        self.word_bank = self.logic_layer.get_word_bank()

    def output(self) -> None:
        self.screen.clear_screen()
        print(LOGO)
        self.list_all_users()
        print(f"\n[C]reate new user   [W]rite new Word   [Q]uit")
        print()

    def list_all_users(self):
        print(f"{SPACING} ╔══───··")
        for (key, value) in self.users.items():
            print(f"{SPACING} ║ {key}. {value}")
        print(f"{SPACING} ╚═════───···")

    def input_prompt(self) -> None:
        self.output()
        user_input = input("Select user index: ").lower()
        while user_input != "q":
                if user_input.lower() == "c":
                    self.create_new_user()
                elif user_input in self.users:
                    # self.invoke_play_menu()
                    user = self.users[user_input]
                    play_menu = UserMenu(user, user_input, self.word_bank) 
                    play_menu.input_prompt()
                
                elif user_input.lower() == "w":
                    self.write_word()
                    
                else:
                    self.output()
                    user_input = input("Please enter a valid command: ")
                    
                self.output()
                user_input = input("Select user index: ").lower()

    def create_new_user(self):  
        while True:
            self.screen.clear_screen()
            print(LOGO)
            print("Usernames must be between 1 - 15 letters")
            new_user = input("\n(C)ancel\nEnter desired username: ")
            if new_user.lower() == "c": return
            if len(new_user) > 1 and len(new_user) < 15: break

        self.logic_layer.save_new_user(new_user)
        self.users = self.logic_layer.get_all_users()


    def write_word(self):
        while True:
            self.screen.clear_screen()
            print(LOGO)
            print("New word must be between 3 - 10 letters")
            new_word = input("\n(C)ancel\nEnter desired word: ")
            if new_word.lower() == "c": return
            if len(new_word) > 1 and len(new_word) < 15: break

        self.logic_layer.write_word(new_word)
