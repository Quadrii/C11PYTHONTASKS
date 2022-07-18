try:
    num = int(input("Enter a number"))
    print(num)
except ValueError:
    print("That was not a number")

number =3
text = "Hello there"
check_num = text[number]
print(check_num)