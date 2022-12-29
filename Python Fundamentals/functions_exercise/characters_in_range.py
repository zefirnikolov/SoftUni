def ascii_printer(start, end):
    int_ascii_start = ord(start)
    int_ascii_end = ord(end)
    ascii_str = ''
    for i in range(int_ascii_start + 1, int_ascii_end):
        ascii_str += chr(i)
    result = ' '.join(ascii_str)
    return result


ascii_start = input()
ascii_end = input()
print(ascii_printer(ascii_start, ascii_end))

# ascii_start = input()
# ascii_end = input()
# int_ascii_start = ord(ascii_start)
# int_ascii_end = ord(ascii_end)
#
# for i in range(int_ascii_start + 1, int_ascii_end):
#     ascii_letter = chr(i)
#     print(ascii_letter, end=" ")
