from decimal import Decimal

a = Decimal('0.1')
b = Decimal('0.1')
c = Decimal('0.1')

print((a + b + c))

list_one = [1, 5, 'Python', 0.5, 55, True, int, 'Pesho']
print(type(list_one))
print(list_one)
list_one[3] = 'Johny'
print(list_one)
list_one[-1] = 17
print(list_one)

tuple_one = (1, 5, 6.5, 'Pes', 'Gogo', False)
print(type(tuple_one))
print(tuple_one)
# tuple_one[4] = 'Ok' - if It's a tuple it can't be modified!

set_one = {'a', 'b', 'c', 'c', 5, 5}
print(type(set_one))
print(set_one)

dictionary_one = {'name': 'pepi', 'age': 10, 'price': 10.5}
print(type(dictionary_one))
print(dictionary_one)

reversed_list = list_one[3 - 1:4:]

if 55 in list_one:
    print("fine")

print(reversed_list)
variable = 42
print(variable)
variable = 'bar'
print(variable)
variable = True
print(variable)

text = 'abc'
print(text[::-1])
