import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"    
)

cursor = con.cursor()

word = input("Please, insert a word:>> ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '{}'" .format(word))
results = cursor.fetchall()

query_test = cursor.execute("SELECT * FROM Dictionary WHERE Expression LIKE '{}%'".format(word[:3]))
results_test = dict(cursor.fetchall())

if results:
    for result in results:
        print(result[1])
elif len(get_close_matches(word, results_test.keys(), cutoff=0.8)) > 0:
    yn = input("Did you mean %s instead? Enter \"Y\" if Yes, or \"N\" if no:>>"  % get_close_matches(word, results_test.keys(), cutoff=0.8)[0])
    yn = yn.upper()
    if yn == 'Y':
        query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '{}'" .format(get_close_matches(word, results_test.keys(), cutoff=0.8)[0]))
        results = cursor.fetchall()
        for result in results:
            print(result[1])           
    elif yn =='N':
        print("Sorry, the expression is not in the dictionary. Please, search for any mistake.")
    else:
        print("Sorry, we did not understand your entry.")
else:
    print("Sorry, this expression is not in the dictionary. Please, search for any mistake")