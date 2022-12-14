olympic_quota__minutes = int(input())
olympic_quota__seconds = int(input())
skeleton_length = float(input())
seconds_per_100_m = int(input())

quota_to_reach = olympic_quota__minutes * 60 + olympic_quota__seconds
slowing = skeleton_length / 120
total_reduced_time = slowing * 2.5
marin_time = (skeleton_length / 100) * seconds_per_100_m - total_reduced_time

difference = abs(quota_to_reach - marin_time)

if marin_time <= quota_to_reach:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {marin_time:.3f}.")
else:
    print(f"No, Marin failed! He was {difference:.3f} second slower.")
