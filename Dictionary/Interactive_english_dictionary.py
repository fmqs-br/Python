import json
from difflib import get_close_matches

data = json.load(open("Dictionary\data.json"))

def dictionary(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
        yn = input("Did you mean %s instead? Enter \"Y\" if Yes, or \"N\" if no:>>"  % get_close_matches(w, data.keys(), cutoff=0.8)[0])
        yn = yn.upper()
        if yn == 'Y':
            return data[get_close_matches(w, data.keys(), cutoff=0.8)[0]]
        elif yn == 'N':
            return "Sorry, the expression is not in the dictionary. Please, search for any mistake."
        else:
            return "Sorry, we did not understand your entry."
    else:
        return "Sorry, the expression is not in the dictionary. Please, search for any mistake."

word = input("Please, enter the word:>>")

print(dictionary(word))