integer = int(input("Enter a number: "))
num_square = integer * integer
print(num_square)
if num_square > 100:
    print("The square of this number is greater than 100")
elif num_square < 100:
    print("The square of this number is not up to 100")
else:
    print("The number is equal to 100")