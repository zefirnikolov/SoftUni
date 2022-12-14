excursion_price = float(input())
puzzles = int(input())
dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

puzzles_sum = puzzles * 2.6
dolls_sum = dolls * 3
teddy_bears_sum = teddy_bears * 4.1
minions_sum = minions * 8.2
trucks_sum = trucks * 2

sum_of_all_toys = puzzles_sum + dolls_sum + teddy_bears_sum + minions_sum + trucks_sum
number_of_all_toys = puzzles + dolls + teddy_bears + minions + trucks

if number_of_all_toys >= 50:
    sum_of_all_toys = sum_of_all_toys - sum_of_all_toys * 0.25

sum_of_all_toys = sum_of_all_toys - sum_of_all_toys * 0.1

if sum_of_all_toys >= excursion_price:
    print(f"Yes! {(sum_of_all_toys - excursion_price):.2f} lv left.")
else:
    print(f'Not enough money! {(excursion_price - sum_of_all_toys):.2f} lv needed.')
