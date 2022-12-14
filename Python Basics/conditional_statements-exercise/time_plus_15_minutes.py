enter_hours = int(input())
enter_minutes = int(input())

hours_to_minutes = enter_hours * 60

all_minutes_plus_15 = hours_to_minutes + enter_minutes + 15

hours = all_minutes_plus_15 // 60
minutes = all_minutes_plus_15 % 60

if hours == 24 and minutes <= 15:
    hours = 0

print(f'{hours}:{minutes:02d}')
