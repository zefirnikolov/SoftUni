record_in_seconds = float(input())
meters = float(input())
time_in_seconds_per_meter = float(input())

time = time_in_seconds_per_meter * meters
slowing_because_of_tide = (meters // 15) * 12.5
all_time = time + slowing_because_of_tide

difference = abs(all_time - record_in_seconds)
if all_time < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {all_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")
