junk_words = ["torture", "thread", "plastic", "needle", "nylon", "biro"]

# Method 1
if junk_words.__contains__("needle"):
    print("found the needle at index", junk_words.index("needle"))
else:
    print("Not found")

# Method 2
find_word = "needle"
if find_word in junk_words:
    print("find", find_word, "at index", junk_words.index(find_word))
else:
    print(find_word, "Not found")
