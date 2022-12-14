chicken_menus = int(input())
fish_menus = int(input())
veg_menus = int(input())

sum_without_desert = chicken_menus * 10.35 \
                     + fish_menus * 12.4 \
                     + veg_menus * 8.15
desert = sum_without_desert * 0.2
delivery = 2.5

sum_of_all = delivery + desert + sum_without_desert
print(sum_of_all)
