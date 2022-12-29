year = int(input())

is_unique_year = False

while not is_unique_year:
    year += 1
    list_of_years = []
    year_check = year
    is_unique_element = True
    while year_check > 0:
        remaining_digit = year_check % 10
        list_of_years.append(remaining_digit)
        year_check = int(year_check / 10)

    for element in list_of_years:
        if list_of_years.count(element) > 1:
            is_unique_element = False
            break

    if is_unique_element:
        is_unique_year = True

print(year)
