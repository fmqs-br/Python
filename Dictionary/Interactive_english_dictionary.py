import json

data = json.load(open("Dictionary\data.json"))

def dictionary(word):
    return data[word]

word = input("Please, enter the word:>>")

print(dictionary(word))

