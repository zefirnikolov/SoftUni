string_1 = input()
string_2 = input()

last_string = string_1

for index_eq_symbol in range(len(string_2)):
    left_part = string_2[0: index_eq_symbol + 1: 1]  # [:index_eq_symbol + 1] - кратко записване! Дължина
    right_part = string_1[index_eq_symbol + 1: len(string_1): 1]  # [index_eq_symbol + 1:] - кратко записване! Начало
    current_string = left_part + right_part

    if current_string == last_string:
        continue

    last_string = current_string
    print(current_string)
