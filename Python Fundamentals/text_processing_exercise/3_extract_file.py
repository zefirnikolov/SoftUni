# file = [element for element in input().split(chr(92)) if "." in element]
file = [element for element in input().split('\\') if '.' in element]  # input.spilt("\\") - will split only to 1 "\"
file_name, file_extension = file[0].split('.')
print(f"File name: {file_name}")
print(f"File extension: {file_extension}")
