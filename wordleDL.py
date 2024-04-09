import random
import csv
class WordleDL:
    def load_all_words(self):
        ret_dict = {}
        with open("word-bank.txt") as file:
            for word in file.readlines():
                if len(word.strip()) not in ret_dict:
                    ret_dict[len(word.strip())] = [word.strip()]
                    continue

                ret_dict[len(word.strip())].append(word.strip())
        
        return ret_dict
    
    def load_scores(self):
        ret_list = []
        with open('scores.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                ret_list.append((row['username'], int(row['score'])))

        return ret_list

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