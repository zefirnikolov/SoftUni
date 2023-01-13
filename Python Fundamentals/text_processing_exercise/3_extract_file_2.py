new_list = input().split("\\")
file_list = [ele.split(".") for ele in new_list if "." in ele]
print(f"File name: {file_list[0][0]}")
print(f"File extension: {file_list[0][1]}")
