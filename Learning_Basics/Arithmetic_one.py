num1 = int(input("Enter a number: "))
print(num1)
num2 = int(input("Enter another number: "))
print(num2)
num3= int(input("Enter the third number: "))
print(num3)
sum = num1 + num2 + num3
print(sum)
product = num1 * num2 * num3
print(product)
average = sum/3
print(average)
smallest = num1
if (num2 < smallest):
    smallest = num2
elif (num3 < smallest):
    smallest = num3
else:
    smallest = num1
print(smallest)
largest = num1
if (num2 > smallest):
    largest = num2
elif (num3 > smallest):
    largest = num3
else:
    largest = num1
print(largest)