num = int(input("Enter a number from (10 above)"))
for i in range(num, 1, -1):
    if num % i == 0:
        print(i, "is a factor of ", num)
    else:
        print(i ,"is not a factor of ", num)