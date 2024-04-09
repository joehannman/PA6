from wordleDL import WordleDL
import random

class WordleLL:
    def __init__(self) -> None:
        self.data_wrapper = WordleDL()

    def get_word(self, length=5):
        words = self.data_wrapper.load_all_words()

        return random.choice(words[length])
    
    def get_all_users(self):
        return self.data_wrapper.load_all_users()

    def save_new_user(self, new_user):
        userId = len(self.get_all_users()) + 1
        self.data_wrapper.save_user(userId, new_user)

    def write_word(self):
        pass

    def get_scores(self):
        score_list = self.data_wrapper.load_scores()
        
        return sorted(score_list, key=lambda item: item[1], reverse=True)
        
    