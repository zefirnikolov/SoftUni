key = int(input())
number_of_loops = int(input())

message = ''
for i in range(number_of_loops):
    letter = input()
    message += chr(key + ord(letter))

print(message)
