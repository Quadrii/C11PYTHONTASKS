# Question: You were camping with your friends far away from home, but when it's time to go back, you realize that
# your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25
# miles per gallon. There are 2 gallons left.
def calc_distance(available_gallons, miles_per_gallon, distance_to_pump):
    calc_distance = available_gallons * miles_per_gallon
    if calc_distance == distance_to_pump:
        print("True")
    else:
        print("False")


calc_distance(2, 25, 50)
