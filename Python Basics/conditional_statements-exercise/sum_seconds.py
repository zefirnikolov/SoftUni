seconds1 = int(input())
seconds2 = int(input())
seconds3 = int(input())

total_time = seconds1 + seconds3 + seconds2

minutes = total_time // 60
seconds = total_time % 60

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')

print(f'{minutes:02d}:{seconds:02d}')