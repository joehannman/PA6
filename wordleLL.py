from wordleDL import WordleDL
import random

class WordleLL:
    def __init__(self) -> None:
        self.data_wrapper = WordleDL()

    def get_word_bank(self):
        words = self.data_wrapper.load_all_words()

        return words
    
    def get_word(self, word_bank, length):
        return random.choice(word_bank[length])
    
    def get_all_users(self):
        return self.data_wrapper.load_all_users()

    def save_new_user(self, new_user):
        userId = len(self.get_all_users()) + 1
        self.data_wrapper.save_user(userId, new_user)

    def write_word(self, word):
        if len(word) < 3 or len(word) > 10: return
        if word in self.get_word_bank()[len(word)]: return
        self.data_wrapper.save_new_word(word)
        
    def get_scores(self):
        score_list = self.data_wrapper.load_scores()
        
        return sorted(score_list, key=lambda item: item[1], reverse=True)
    
    def get_scores_by_player(self, username):
        score_list = self.data_wrapper.load_scores()
        ret_list = []
        for score in score_list:
            if score[0] == username:
                ret_list.append(score)
        
        return sorted(ret_list, key=lambda item: item[1], reverse=True)
    
    def validate_guess(self, guess, word):
        try:
            int(guess)
            return False
        
        except ValueError:
            if len(guess) != len(word):
                return False
            
            return True

    
    def check_for_win(self, guess, word):
        if guess.lower() == word.lower():
            return True
        
        return False

    def save_score(self, user, score):
        self.data_wrapper.store_score(user, score)

    def get_player_scores(self):
        return self.data_wrapper.load_player_scores()
    
    def validate_word_length(self, wordlength):
        try:
            wordlength = int(wordlength)

            if wordlength < 3 or wordlength > 10:
                return False
            
            return True
        
        except ValueError:
            return False
    
