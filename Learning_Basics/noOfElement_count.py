import string
def histogram(word) -> dict[str, int]:
    abc = string.ascii_lowercase
    map_ = {}
    for char in abc:
        map_[char] = word.lower().count(char)
    return map_

check = histogram("Alabama is a town")
print(check)