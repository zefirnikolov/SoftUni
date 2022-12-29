values = input().split("#")
water = int(input())

total_fire = 0
effort = 0

print("Cells:")
for ele in values:
    new_list = ele.split(" = ")
    type_of_fire = ''

    for index, element in enumerate(new_list):
        if element == "High":
            type_of_fire = "High"
            continue
        elif element == "Medium":
            type_of_fire = "Medium"
            continue
        elif element == "Low":
            type_of_fire = "Low"
            continue

        if type_of_fire == "High" and 81 <= int(element) <= 125:
            total_fire += int(element)
            if total_fire > water:
                total_fire -= int(element)
                continue
            else:
                effort += int(element) * 0.25
                print(f" - {int(element)}")

        if type_of_fire == "Medium" and 51 <= int(element) <= 80:
            total_fire += int(element)
            if total_fire > water:
                total_fire -= int(element)
                continue
            else:
                effort += int(element) * 0.25
                print(f" - {int(element)}")

        if type_of_fire == "Low" and 1 <= int(element) <= 50:
            total_fire += int(element)
            if total_fire > water:
                total_fire -= int(element)
                continue
            else:
                effort += int(element) * 0.25
                print(f" - {int(element)}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
