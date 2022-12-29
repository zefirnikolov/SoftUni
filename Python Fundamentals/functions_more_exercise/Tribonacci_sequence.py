def tribonacci_sequence(number_of_loops):
    number_list = []
    for number in range(number_of_loops):
        if number == 0:
            number_list.append(1)
        elif len(number_list) == 1:
            number_list.append(number)
        elif len(number_list) == 2:
            number_list.append(number)
        else:
            result = number_list[-1] + number_list[-2] + number_list[-3]
            number_list.append(result)
    return " ".join([str(x) for x in number_list])


num = int(input())
print(tribonacci_sequence(num))
