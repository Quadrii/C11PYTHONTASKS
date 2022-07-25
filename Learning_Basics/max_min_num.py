#Question: Your task is to make two functions ( max and min, or maximum and minimum, etc., depending on the language ) that receive a list of integers as input, and return the largest and lowest number in that list, respectively.

arr_num = [2,3,4,6,8,9,23,45]
maximum_num = arr_num[0]
for num in arr_num:
    if num > maximum_num:
        maximum_num = num
print(maximum_num)

arr_nums = [2,3,4,6,8,9,45]
minimum_num = arr_nums[0]
for number in arr_nums:
    if number < minimum_num:
        minimum_num = number
print(minimum_num)