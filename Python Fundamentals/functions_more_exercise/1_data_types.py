def types_data_func(command, value):
    if command == "int":
        return int(value) * 2
    elif command == 'real':
        return f"{(float(value) * 1.5):.2f}"
    elif command == 'string':
        return f"${value}$"


variable_type = input()
variable = input()
print(types_data_func(variable_type, variable))
