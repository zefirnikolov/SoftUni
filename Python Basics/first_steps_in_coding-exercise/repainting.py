# • Предпазен найлон - 1.50 лв. за кв. метър
# • Боя - 14.50 лв. за литър
# • Разредител за боя - 5.00 лв. за литър
# За всеки случай, към необходимите материали, Румен иска да добави още 10% от количеството боя и 2 кв.м.
# найлон, разбира се и 0.40 лв. за торбички. Сумата, която се заплаща на майсторите за 1 час работа, е равна
# на 30% от сбора на всички разходи за материали.

nylon_needed = int(input())
paint_needed = int(input())
water_needed = int(input())
hours_work = int(input())

sum_for_nylon = (nylon_needed + 2) * 1.5
sum_for_paint = (paint_needed + paint_needed * 0.1) * 14.5
sum_for_water = water_needed * 5
sum_for_bags = 0.4

materials_sum = sum_for_bags + sum_for_water + sum_for_paint + sum_for_nylon
workers_sum = materials_sum * 0.3 * hours_work
all_sum = materials_sum + workers_sum
print(all_sum)
