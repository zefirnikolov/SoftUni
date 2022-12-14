deposited_sum = float(input())
months = int(input())
interest_rate = float(input())

sum_of_deposit = deposited_sum + months * ((deposited_sum * interest_rate / 100) / 12)
print(sum_of_deposit)
