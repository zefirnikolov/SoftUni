is_five_o_clock = False

for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(f"{hours}:{minutes}:{seconds}")
            if hours == 5:
                is_five_o_clock = True
                break
        if is_five_o_clock:
            break
    if is_five_o_clock:
        break
