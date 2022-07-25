import random

capitals_dic = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock"
}

state, capital = random.choice(list(capitals_dic.items()))
while True:
    guess = input(f"what is the capital of '{state}'? ").lower()
    if guess == "exit":
        print(f"The capital of '{state}' is '{capital}'. ")
        print("GoodBye")
        break
    elif guess == capital.lower():
        print("Correct! nice job")
        break

