university = [
    ["caliphonia institude of technology", 2175, 37704],
    ["Harvad", 19767, 39849],
    ["Princeton", 7802, 37000],
    ["Massachusetts Institute of Technology", 10566, 40732],
    ["Rice", 5879, 355511],
    ["Stamford", 19535, 40569],
    ["Yale", 11701, 40500]
]

def enrollment_stat(university_name, num_of_enrolled_students, annual_tuition_fee):
    return num_of_enrolled_students[1][1], annual_tuition_fee[1][1]

testing = enrollment_stat(university, university, university)
print(testing)