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
    
    def write_word(self):
        pass