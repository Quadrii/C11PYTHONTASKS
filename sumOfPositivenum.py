#Question: You get an array of numbers, return the sum of all of the positives ones.
array_num = [2,3,6,8,-10,-3,0,-3,64,25]
positive_sum = 0
for i in array_num:
    if i > 0:
        positive_sum = positive_sum + i
print(positive_sum)
