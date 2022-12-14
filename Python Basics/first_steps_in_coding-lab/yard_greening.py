m2_for_greening = float(input())

price_for_1_m2 = 7.61

without_discount_price = (m2_for_greening * price_for_1_m2)
final_price = without_discount_price - without_discount_price * 0.18
price_with_discount = without_discount_price * 0.18

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {price_with_discount} lv.")
