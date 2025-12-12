import random
import requests
import json
# maybe import requests later for API
# maybe import color stuff
# Pull a secret word via an API
def pullwordlist():
    url = "https://www.wordgamedb.com/api/v2/words"
    response = requests.get(url)
    # Check to see if data is pulled, if so continue. Report failed status.
    if response.status_code == 200:
        wordlist = response.json()
        print(json.dumps(wordlist, indent=2))
        return wordlist
    else:
        print(f'Error code: {response.status_code}')
    return
wordlist = pullwordlist()
if wordlist is None:
    exit()  # or handle error how you want

# this is the list of word objects from the JSON
worddir = wordlist['words']


def get_random_word(wordlist):
    # wordlist here is already a LIST like:
    # [ {"word": "cobra", ...}, {"word": "tiger", ...}, ... ]

    # just pick ONE random object from the list
    random_entry = random.choice(wordlist)

    # then grab its "word" field (a full string, e.g. "cobra")
    answer = random_entry['word']

    return answer


answer = get_random_word(worddir)
print(answer)