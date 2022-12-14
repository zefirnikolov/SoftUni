length = int(input())
width = int(input())
height = int(input())
percent_taken_in_the_tank = float(input())

m3_of_the_tank = length * width * height
m3_in_liters = m3_of_the_tank * 0.001
percent_taken_in_the_tank = percent_taken_in_the_tank / 100
liters_needed = m3_in_liters * (1 - percent_taken_in_the_tank)

print(liters_needed)
