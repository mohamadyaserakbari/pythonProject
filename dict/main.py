import json
from difflib import *

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        ans = input("Did you mean %s instead?(Y/N)" % get_close_matches(w, data.keys())[0])
        ans = ans.lower()
        if ans == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        elif ans == 'n':
            return "The word doesn't exists. please check it out!"
        else:
            breakpoint()
    else:
        print("The word doesn't exist please check again.")


word = input("Enter your word here:")
output = (translate(word))
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)