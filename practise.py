from functools import reduce
lst = [1, 2, 3, 4]

rng = range(1, 100, 5)
print(rng)
fruits = ['yellow', "blue", "cat", "large", "apple", "cucumber", "pineapple"]
lst_rng = list(range(1, 100, 5))
lst_rng.append(1_000)
lst_rng.extend([2, 3, 5, 6])
print(lst_rng)
check_max = max('yellow', "blue", "cat", "large", "apple")
check_min = min('yellow', "blue", "cat", "large", "apple")
num = [2, 4, 6, 5, 3, 67, 34, 56, 33]
for i in num:
    if i % 2 == 0:
        print("is even", [i])
    else:
        print("not even numbers", [i])
# Generator expressions
numbers = [1, 2, 3, 4, 56, 12, 34, 6]
reversed_num = [x for x in reversed(numbers)]
for value in (x ** 2 for x in numbers if x % 2 == 0):
    print(value, end=' ')
def sub(a=0, b=0):
    return b-a
generator = (x ** 2 for x in numbers if x % 2 == 0)
# List Comprehension
comprehenson = [x ** 2 for x in numbers if x % 2 == 0]
lamb=(lambda x, y: x + y )
lst=[1,2,4,5,7]
all(True if i >= 7 else False for i in lst)
list_of_dict = [{"name": "Asake", "gender":"F"}, {"name":"Boyo", "gender":"M"}]
mapped_list = map(lambda x: ("Mr. " if x["gender"] == "M" else "Mrs. ") + x["name"], list_of_dict )
filter_list = list(filter(lambda x:x["gender"] == "M", list_of_dict))
sum_reduce = reduce(lambda acc, value: acc + value, numbers)
print(filter_list)
print(mapped_list)
print([("Mr. " if x["gender"] == "M" else "Mrs. ") + x["name"] for x in list_of_dict])
print(i)
print(lamb)
print(generator)
print(comprehenson)
print(reversed_num)
print(check_max)
print(check_min)
print(sum_reduce)
print(reduce(lambda x,y: x if len(x) > len(y) else y, fruits))
print(sub(b=10, a=15))
assert 4 == 3, "the two numbers must be equal"
# for ls in lst_rng:
#     if ls % 2 == 0:
#         lst_rng.remove(ls)
#     elif ls % 2 != 0:
#         print(ls)
