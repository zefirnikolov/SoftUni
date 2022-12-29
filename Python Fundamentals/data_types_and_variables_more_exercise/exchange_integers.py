integer_one = int(input())
integer_two = int(input())

element_list = [integer_one, integer_two]
print("Before:")
print(f"a = {element_list[0]}")
print(f"b = {element_list[1]}")
element_list[0], element_list[1] = element_list[1], element_list[0]
print("After:")
print(f"a = {element_list[0]}")
print(f"b = {element_list[1]}")
