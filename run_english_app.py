import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def definition(input_word):
    input_word = input_word.lower()             # converting the words to lower case as dictionary has all words so
    if input_word in data:
        return data[input_word]

    elif len(get_close_matches(input_word, data.keys())) > 0:           # to get the approx close word possible,
        # output of this method is a list and if the len is > 0, the first word would be most close match

        matching_word = get_close_matches(input_word, data.keys())[0]
        confirm = "Did you mean {} instead?"
        print(confirm.format(matching_word))
        yn = input("Enter Y is yes or N if no: ")
        if yn == 'Y':
            return data[matching_word]
        elif yn == 'N':
            return "The word does not exist"
        else:
            return "Invalid input"
    else:
        return "The word does not exist"                # for mismatch words


word = input("Enter the word: ")
output = definition(word)

for out in output:
    if type(output) == list:
        print(out)
    else:
        print(output)

