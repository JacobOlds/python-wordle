import random
import requests
import json
from collections import Counter

# Pull a secret word via an API
def pullwordlist():
    url = "https://www.wordgamedb.com/api/v2/words"
    response = requests.get(url)
    # Check to see if data is pulled, if so continue. Report failed status.
    if response.status_code == 200:
        wordlist = response.json()
        # print(json.dumps(wordlist, indent=2))
        # Uncomment line above to print the json for debug.
        return wordlist
    else:
        print(f"Error code: {response.status_code}")
        return None


# Define our wordlist then handle if the list is empty.
wordlist = pullwordlist()
if wordlist is None:
    exit()  # Will exit to prevent code running w/ empty list.

# this is the list of word objects from the JSON
# adjust this if the API structure is different
worddir = wordlist["words"]


# Pick a word randomly from our wordlist.
def get_random_word(wordlist):
    # Grab random word via random
    random_entry = random.choice(wordlist)
    # then grab its "word" field (a full string, e.g. "cobra")
    answer = random_entry["word"]
    return answer.lower()


answer = get_random_word(worddir)


# Defines how many guesses the player will get.
# Based on len(answer).
def player_guess_count(answer):
    return len(answer)


max_guesses = player_guess_count(answer)

# Color one guess in Wordle style
def colorize_guess(guess: str, answer: str) -> str:
    guess = guess.lower()
    answer = answer.lower()

    GREEN = "\033[92m"   # bright green
    YELLOW = "\033[93m"  # yellow
    GRAY = "\033[90m"    # gray
    RESET = "\033[0m"

    result = []
    length = len(answer)

    # First pass: mark greens, track remaining letters for yellows
    remaining = Counter()
    colors = ["gray"] * length

    for i in range(length):
        if guess[i] == answer[i]:
            colors[i] = "green"
        else:
            remaining[answer[i]] += 1

    # Second pass: yellows vs gray
    for i in range(length):
        letter = guess[i]
        if colors[i] == "green":
            result.append(f"{GREEN}{letter}{RESET}")
        elif remaining[letter] > 0:
            remaining[letter] -= 1
            result.append(f"{YELLOW}{letter}{RESET}")
        else:
            result.append(f"{GRAY}{letter}{RESET}")

    return "".join(result)


# Player guesses + Main functionality of game.
def player_guess(answer, max_guesses):
    currentguesscounter = 0
    word_len = len(answer)

    print("Welcome to Wordle!")
    print(f"The word has {word_len} letters. You have {max_guesses} guesses.\n")

    while currentguesscounter < max_guesses:
        guess = input("Enter in your guess: ").strip().lower()

        # basic validation of length of guess and answer being same length.
        if len(guess) != word_len:
            print(f"Invalid guess, your word will need to be {word_len} characters long.\n")
            continue
        
        # basic validation of characters. only english characters:
        if not guess.isalpha():
            print("Invalid guess: only A–Z letters are allowed.\n")
            continue

        currentguesscounter += 1

        # Show colored feedback
        print(colorize_guess(guess, answer))

        # Player guessed the right answer, they win.
        if guess == answer:
            print(f"\nCongratulations you guessed {answer} correctly in {currentguesscounter} tries!")
            return

        remaining = max_guesses - currentguesscounter
        if remaining > 0:
            print(f"You have {remaining} guesses left.\n")

    # If we exit the loop without returning, player is out of guesses.
    print(f"\nYou lost! The word was: {answer}")

def play_game():
    # pick a NEW random answer every time this function runs
    answer = get_random_word(worddir)
    max_guesses = player_guess_count(answer)

    # OPTIONAL: show the answer for debugging
    #print(f"DEBUG — answer is: {answer}")

    # run the Wordle gameplay loop
    player_guess(answer, max_guesses)

# Start game
def main():
    while True:
        play_game()

        playagain = input("Would you like to play again? (yes/no): ").strip().lower()
        if playagain == "yes":
            continue
        elif playagain == "no":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            # you can loop back to ask again or just continue to next iteration


# Debug: show answer while testing
#print("DEBUG – answer is:", answer)


if __name__ == "__main__":
    main()
