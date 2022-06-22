junk_words = ["torture", "thread", "plastic", "needle", "nylon", "biro"]
for i in junk_words:
    if  junk_words.__contains__("needle"):
        print("found the needle at", junk_words.index("needle"))
    else:
        print("Not found")
