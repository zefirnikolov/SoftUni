flower = input()
number_of_flowers = int(input())
budget = int(input())

rose_price = 5
dahlia_price = 3.8
tulip_price = 2.8
narcissus_price = 3
gladiolus_price = 2.5

sum_of_all_flowers = 0

if flower == "Roses":
    sum_of_all_flowers = number_of_flowers * rose_price
    if number_of_flowers > 80:
        sum_of_all_flowers *= 0.9

elif flower == "Dahlias":
    sum_of_all_flowers = number_of_flowers * dahlia_price
    if number_of_flowers > 90:
        sum_of_all_flowers *= 0.85

elif flower == "Tulips":
    sum_of_all_flowers = number_of_flowers * tulip_price
    if number_of_flowers > 80:
        sum_of_all_flowers *= 0.85

elif flower == "Narcissus":
    sum_of_all_flowers = number_of_flowers * narcissus_price
    if number_of_flowers < 120:
        sum_of_all_flowers *= 1.15

elif flower == "Gladiolus":
    sum_of_all_flowers = number_of_flowers * gladiolus_price
    if number_of_flowers < 80:
        sum_of_all_flowers *= 1.2

difference = abs(sum_of_all_flowers - budget)

if sum_of_all_flowers <= budget:
    print(f"Hey, you have a great garden with {number_of_flowers} {flower} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
