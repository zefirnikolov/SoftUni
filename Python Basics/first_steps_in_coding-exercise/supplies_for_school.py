# • Пакет химикали - 5.80 лв.
# • Пакет маркери - 7.20 лв.
# • Препарат - 1.20 лв (за литър)

packets_pens = int(input())
packets_markers = int(input())
packets_washing_liquid = int(input())
discount_in_percent = int(input())

pen_price = 5.8
marker_price = 7.2
washing_liquid_price = 1.2

all_pens_price = pen_price * packets_pens
all_markers_price = marker_price * packets_markers
all_liquid_price = washing_liquid_price * packets_washing_liquid

sum_of_all = all_liquid_price + all_markers_price + all_pens_price
sum_with_discount = sum_of_all - sum_of_all * discount_in_percent / 100

print(f"{sum_with_discount:.2f}")
