import random

capitals_dic = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock"
}

randoms = random.choice(capitals_dic.items())
print(randoms)
