hour_of_exam = int(input())
minute_of_exam = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

if hour_of_exam == 0:
    hour_of_exam = 24

if hour_of_arrival == 0:
    hour_of_arrival = 24

time_of_exam_in_minutes = hour_of_exam * 60 + minute_of_exam
time_of_arrival_in_minutes = hour_of_arrival * 60 + minute_of_arrival

difference = time_of_exam_in_minutes - time_of_arrival_in_minutes
abs_difference = abs(difference)
is_on_time = 0 <= difference <= 30
is_late = difference < 0

late_or_early_in_minutes = abs(time_of_arrival_in_minutes - time_of_exam_in_minutes)
hours_late_or_early = late_or_early_in_minutes // 60
minutes_late_or_early = late_or_early_in_minutes % 60

if is_on_time:
    print("On time")
    if difference == 0:
        pass
    else:
        print(f"{difference} minutes before the start")
elif is_late:
    print("Late")
    if abs_difference <= 59:
        print(f"{abs_difference} minutes after the start")
    else:
        print(f"{hours_late_or_early}:{minutes_late_or_early:02d} hours after the start")
else:
    print("Early")
    if difference <= 59:
        print(f"{difference} minutes before the start")
    else:
        print(f"{hours_late_or_early}:{minutes_late_or_early:02d} hours before the start")
