from assets.jokes import jokes_list
from assets.quotes import quotes_list
import time
import random


# times.sleep(5)
# print(jokes_list[0])

def jokeBot():
    print("Do you want to hear a joke?")
    user_input = input()
    if user_input == "y":
        this_joke = random.choice(jokes_list)
        print("Okat let me think...")
        time.sleep(2)
        print(this_joke["setup"])
        time.sleep(5)
        print(this_joke["punchline"])
        time.sleep(2)
        jokeBot()
    elif user_input == "n":
        print("Awwwwwww Ok")
    else:
        print("I couldn't what you said")


jokeBot()
