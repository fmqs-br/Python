import json
from difflib import get_close_matches

data = json.load(open("Dictionary\data.json"))

def dictionary(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
        return "Did you mean %s instead?" % get_close_matches(w, data.keys(), cutoff=0.8)[0]
    else:
        return "Sorry, the expression is not in the dictionary. Please, search for any mistake."

word = input("Please, enter the word:>>")

print(dictionary(word))    
       
    


