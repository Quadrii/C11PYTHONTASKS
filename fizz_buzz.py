number= int(input("Enter a number between 1-100: "))
if number % 5 == 0 and number % 3 == 0:
    print("fizzBuzz")
elif number % 3 == 0:
    print("fizz")
elif number % 5 == 0:
    print("buzz")
else:
    print(number, "Not divisible by 3 and 5")


