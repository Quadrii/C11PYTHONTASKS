universities = [
    ["caliphonia institude of technology", 2175, 37704],
    ["Harvad", 19767, 39849],
    ["Princeton", 7802, 37000],
    ["Massachusetts Institute of Technology", 10566, 40732],
    ["Rice", 5879, 355511],
    ["Stamford", 19535, 40569],
    ["Yale", 11701, 40500]
]


def enrollment_stat(list_of_universities):
    total_student = []
    total_tuition = []
    for university in list_of_universities:
        total_student.append(university[1])
        total_tuition.append(university[2])
    return total_tuition, total_student


def mean(values):
    return sum(values) / len(values)


def median(values):
    values.sort()
    if len(values) % 2 == 1:
        center_value = int(len(values) / 2)
        return values[center_value]

    else:
        left_center_index = (len(values) - 1) // 2
        right_center_index = (len(values) - 1) // 2
        return mean([values[left_center_index], values[right_center_index]])


totals = enrollment_stat(universities)
print(f"Student median:   {median(totals[0]):,}")

