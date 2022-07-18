for num in range(2, 10):
    print(num)

count = 2
while count < 10:
    print(count)
    count = count + 1


def doubleFunction(number):
    square = number * 2
    return square



my_num = 2
for i in range(0, 3):
    my_num = doubleFunction(my_num)
    print(my_num)
