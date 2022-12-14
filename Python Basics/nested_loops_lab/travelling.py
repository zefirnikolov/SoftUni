destination = input()

while destination != "End":
    budget = float(input())
    total_save = 0

    while total_save < budget:
        current_save = float(input())
        total_save += current_save

    print(f"Going to {destination}!")
    destination = input()
