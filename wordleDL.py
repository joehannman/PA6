import random
import csv
class WordleDL:
    def load_all_words(self):
        with open("word-bank.txt") as file:
            return [word.strip() for word in file.readlines()]

    def load_scores():
        ret_dict = {}
        with open('scores.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                ret_dict[row['userId']] = row['score']

        return ret_dict

    def load_all_users(self):
        ret_dict = {}
        with open('users.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                ret_dict[row['userId']] = row['UserName']

        return ret_dict
    
    def save_new_score(userId, score):
        with open('users.csv', 'a', newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['userId','score'])
            
            writer.writerow({
                'userId': userId,
                'score': score
            })

    def save_user(self, userId, username):
        with open('users.csv', 'a', newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['userId','UserName'])
            
            writer.writerow({
                'userId': userId,
                'UserName': username
            })

    def save_new_word():
        pass