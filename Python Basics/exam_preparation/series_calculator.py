from math import floor

series_name = input()
seasons = int(input())
number_of_episodes = int(input())
time_per_one_episode = float(input())

ads_time = time_per_one_episode * 0.2
total_time_per_episode = time_per_one_episode + ads_time
special_episodes_added_time = seasons * 10

total_time = total_time_per_episode * number_of_episodes * seasons + special_episodes_added_time

print(f"Total time needed to watch the {series_name} series is {floor(total_time)} minutes.")
