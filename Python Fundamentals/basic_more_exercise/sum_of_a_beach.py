string_input = input()
string_check = string_input.lower()

sun_count = string_check.count('sun')
sand_count = string_check.count('sand')
water_count = string_check.count('water')
fish_count = string_check.count('fish')

total_count = sun_count + sand_count + water_count + fish_count
print(total_count)
