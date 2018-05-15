import json
from difflib import get_close_matches

data = json.load(open("data.json"))
def meaning(word):
    if word in data:
        return data[word]#method of accessing json
    elif len(get_close_matches(word,data.keys()))>0:
        yn = input("Did you mean %s?Enter Y or N : "% get_close_matches(word,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word,data.keys())[0]]

        elif yn =="N":
            return"word not available in the dictionary"
        else:
            return"we do not understand your entry"
    else:
            return"word doesnt exist"
word = input("enter the word: ").lower()#converting to lower case
output = meaning(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
