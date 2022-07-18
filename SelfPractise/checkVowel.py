vowel = ("a", "e", "i", "o", "u")
check_for_vowel = "i am going back to school"
for i in check_for_vowel:
    if i in vowel:
        print(i, "is a vowel")
    elif i == " ":
        print("This is an empty space")
    else:
        print(i, "is not a vowel")
