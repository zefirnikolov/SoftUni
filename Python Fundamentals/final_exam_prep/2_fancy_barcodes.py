import re

number_of_loops = int(input())
search_pattern = r'@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+'

for _ in range(number_of_loops):
    text = input()
    result = re.search(search_pattern, text)
    if result:
        code = ''
        for element in result.group():
            if element.isdigit():
                code += element
        if code:
            print(f'Product group: {code}')
        else:
            print('Product group: 00')
    else:
        print('Invalid barcode')
