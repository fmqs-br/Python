import json

data = json.load(open("Dictionary\data.json"))

def dictionary(w):
    if w in data:
        return data[w]
    else:
        return "Sorry, the expression is not in the dictionary. Please, search for any mistake."

word = input("Please, enter the word:>>")
print(dictionary(word))
       
    


