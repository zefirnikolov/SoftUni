my_dict = {'fruit': 'apple',
           'vegetable': 'cucumber'
           }
print(my_dict)
print(my_dict['fruit'])
print(my_dict.get('vegetable'))
my_dict['vegetable'] = 'potato'
my_dict['meat'] = 'chicken'
print(my_dict)
dict_arguments = dict(name="George", age=22)

print(dict_arguments)
combine = {**my_dict, **dict_arguments}
print(combine)
letters = ['a', 'b', 'c', 'd']
nums = [1, 2, 3, 4]
result = dict(zip(letters, nums))
print(result)
# keys value
for key in my_dict.keys():
    print(key, end=" ")
print()
# values value
for value in my_dict.values():
    print(value, end=" ")
print()
# tuples with combined keys and values
for item in my_dict.items():
    print(item, end=" ")
print()

for key in my_dict.keys():
    print(key, end=" ")
    value = my_dict[key]
    print(value)
print()

for key, value in my_dict.items():
    print(key, value)

if 'vegetable' in my_dict:  # or with my_dict.keys()
    print(f"If vegetable in my_dict: the value of key 'vegetable' = {my_dict['vegetable']}")

if 'chicken' in my_dict.values():
    print('"chicken" is value in the dictionary')

to_delete_keys = [k for k, v in my_dict.items() if not v.isdigit()]
for element in to_delete_keys:
    del my_dict[element]
to_delete_keys.clear()
print(my_dict)
my_dict.update(dict_arguments)
my_dict.update(result)
print(my_dict)
