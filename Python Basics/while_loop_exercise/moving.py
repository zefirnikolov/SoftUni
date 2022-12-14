width = int(input())
length = int(input())
height = int(input())

free_space_in_m3 = width * length * height
blocks_until_Done = input()
total_blocks = 0
is_full = False

while blocks_until_Done != "Done":
    int_blocks = int(blocks_until_Done)
    total_blocks += int_blocks

    if total_blocks > free_space_in_m3:
        is_full = True
        break

    blocks_until_Done = input()

difference = abs(total_blocks - free_space_in_m3)

if is_full:
    print(f"No more free space! You need {difference} Cubic meters more.")
else:
    print(f"{difference} Cubic meters left.")
