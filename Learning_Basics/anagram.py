num = int(input("Enter a number: "))
square_num = num * num
print(square_num)

convert = str(num)

convert_to_str = str(square_num)

checking = convert_to_str.rfind(convert)
if checking == 1:
    print("Its an anagram")
else:
    print("Its not an anagram")

