# Nested dicts
students = {
    1: {'name': 'Peter', 'course': 'programming basics'},
    2: {"name": 'Johnny', 'course': 'fundamentals'},
    3: {'name': 'George', 'course': 'fundamentals'},
    4: {'name': 'Peter', 'is_there': False}
}
# print(students[1])
# print(students[1]['name'])
for key, value in students.items():
    for nested_key, nested_value in value.items():
        print(key, nested_key, nested_value)

example_dict = {'a': 10, 'b': 20, 'c': 30}
comprehension_dict = {key * 2: value * 2 for key, value in example_dict.items()}
print(comprehension_dict)
