quantity = int(input())
days_till_christmas_eq_loops = int(input())

total_cost = 0
spirit_points = 0

# Decoration Price/Piece Points/Shopping
# Ornament Set    2$             5
# Tree Skirt      5$             3
# Tree Garland    3$             10
# Tree Lights     15$            17

ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15

for current_day in range(1, days_till_christmas_eq_loops + 1):

    if current_day % 11 == 0:
        quantity += 2

    if current_day % 2 == 0:
        total_cost += ornament_set * quantity
        spirit_points += 5

    if current_day % 3 == 0:
        total_cost += (tree_skirt + tree_garland) * quantity
        spirit_points += 3 + 10

    if current_day % 5 == 0:
        total_cost += tree_lights * quantity
        spirit_points += 17

    if current_day % 3 == 0 and current_day % 5 == 0:
        spirit_points += 30

    if current_day % 10 == 0:
        spirit_points -= 20
        total_cost += tree_lights + tree_skirt + tree_garland

if days_till_christmas_eq_loops % 10 == 0:
    spirit_points -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {spirit_points}")
