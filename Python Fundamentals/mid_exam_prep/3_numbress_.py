def sorter_func(data):
    average_value = sum(data) / len(data)
    new_list = [num for num in data if num > average_value]
    new_list.sort(reverse=True)
    if len(new_list) > 5:
        new_list = new_list[:4 + 1:]
    if not new_list:
        print("No")
    else:
        print(" ".join(str(num) for num in new_list))


sequence_list = list(map(int, input().split()))
sorter_func(sequence_list)
