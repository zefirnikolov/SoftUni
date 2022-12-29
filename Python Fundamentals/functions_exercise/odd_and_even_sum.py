def odd_and_even_sum(digit):
    digit_list = [int(x) for x in str(digit)]  # make integer list with all the digits
    odd_sums = 0
    even_sums = 0
    for element in digit_list:
        if element % 2 == 1:
            odd_sums += element
        else:
            even_sums += element
    return f"Odd sum = {odd_sums}, Even sum = {even_sums}"


current_number = int(input())
print(odd_and_even_sum(current_number))
