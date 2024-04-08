from wordleDL import WordleDL
import random

class WordleLL:
    def __init__(self) -> None:
        self.data_wrapper = WordleDL()

    def get_word(self, length=5):
        words = self.data_wrapper.load_all_words()
        word_list = []
        for word in words:
            if len(word) == length:
                word_list.append(word)

        return random.choice(word_list)
    
    def get_all_users(self):
        return self.data_wrapper.load_all_users()

    def save_new_user(self, new_user):
        userId = len(self.get_all_users()) + 1
        self.data_wrapper.save_user(userId, new_user)

    def write_word(self):
        pass