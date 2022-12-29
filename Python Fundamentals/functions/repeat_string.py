# some_string = input()
# repeat_times = int(input())
#
# print(some_string * repeat_times)


def repeater(string, repeat):
    result = string * repeat
    return result


some_string = input()
repeat_times = int(input())
print(repeater(some_string, repeat_times))
