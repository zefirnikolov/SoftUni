print('let\'s')
a = """
This is
multiple 
lines string
"""
print(a)
a = 'Test example'
sliced_a = a[:4:]
print(sliced_a)
sliced_a = a[-4::]
print(sliced_a)
sliced_a = a[:-1:]
print(sliced_a)
sliced_a = a[slice(0, 4)]
print(sliced_a)
b = "         Test          "
stripped_b = b.strip()
print(stripped_b)
b = 'This is text example example example'
refined = b.replace('example', '')
print(refined)
refined_with_counter = b.replace('example', '', 1)
print(refined_with_counter)
string = "ewgergh2342354$%^&^*%"
for element in string:
    if 97 <= ord(element) <= 122:
        print("ascii")

new_string = string.replace('%', 'K')
print(new_string)
new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

