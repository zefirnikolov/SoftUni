# numbers = list(map(float, input().split()))
# result = [abs(element) for element in numbers]
# print(result)

# def abs_numbers():
#     new_list = input().split()
#     abs_list = []
#
#     for element in new_list:
#         abs_list.append(abs(float(element)))
#
#     print(abs_list)
#
#
# abs_numbers()

def abs_numbers(num):
    result = [abs(num) for num in numbers]
    return result


numbers = list(map(float, input().split()))
print(abs_numbers(numbers))
