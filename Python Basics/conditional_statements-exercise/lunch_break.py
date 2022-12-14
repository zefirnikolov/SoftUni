from math import ceil

name = input()
length_of_a_series = int(input())
length_of_the_rest = int(input())

lunch_time = length_of_the_rest * 0.125
break_time = length_of_the_rest * 0.25

all_rest = lunch_time + break_time + length_of_a_series

difference = abs(all_rest - length_of_the_rest)
if all_rest <= length_of_the_rest:
    print(f"You have enough time to watch {name} and left with {ceil(difference)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name}, you need {ceil(difference)} more minutes.")
