num = int(input("Enter a number: "))
positive_num=0
negative_num=0
zero_num = 0
num_count=0
while num != -1:
    num = int(input("Enter a number: "))
    if num > 0:
        positive_num= positive_num +1
    elif num < 0:
        negative_num = negative_num + 1
    else:
        zero_num=zero_num+1

print(positive_num)
print(negative_num)
print(zero_num)





