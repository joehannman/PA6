import random
import csv
class WordleDL:
    def load_all_users():
        pass

    def load_all_words(self):
        with open("word-bank.txt") as file:
            return [word.strip() for word in file.readlines()]

    def load_scores():
        pass

    def load_all_users(self):
        ret_dict = {}
        with open('users.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                ret_dict[row['userId']] = row['UserName']

        return ret_dict
    
    def save_new_score():
        pass

    def save_user():
        pass

    def save_new_word():
        pass