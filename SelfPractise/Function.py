def convert_temp(celcious):
    f = celcious * 9 / 5 + 32
    return f;


result = convert_temp(6.8)
print(result)


def convert_temp2(farenheit):
    celc = (farenheit - 32) * 5 / 9
    return celc


result1 = convert_temp2(7.5)
print(result1)
