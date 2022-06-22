lst = [1, 2, 3, 4]

rng = range(1, 100, 5)
print(rng)

lst_rng = list(range(1, 100, 5))
lst_rng.append(1_000)
lst_rng.extend([2, 3, 5, 6])
print(lst_rng)
check_max = max('yellow', "blue", "cat", "large", "apple")
check_min = min('yellow', "blue", "cat", "large", "apple")
num = [2,4,6,5,3,67,34,56,33]
for i in num:
    if i % 2 == 0:
        print("is even", [i])
    else:
        print("not even numbers", [i])


print(check_max)
print(check_min)
# for ls in lst_rng:
#     if ls % 2 == 0:
#         lst_rng.remove(ls)
#     elif ls % 2 != 0:
#         print(ls)