def loading_bar(digit):
    number_of_positive_loads = digit / 10
    percent_load = ''
    for element in range(1, 11):
        if element <= number_of_positive_loads:
            percent_load += "%"
        else:
            percent_load += "."
    if digit == 100:
        return f"{digit}% Complete!\n[{percent_load}]"
    else:
        return f"{digit}% [{percent_load}]\nStill loading..."


number = int(input())
print(loading_bar(number))
