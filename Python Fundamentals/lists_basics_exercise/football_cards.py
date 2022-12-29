cards_notebook = input()

a_team_list = ["A-1", 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11',
               "B-1", 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
red_cards_list = cards_notebook.split()
team_a_red_cards_list = []
team_b_red_cards_list = []
team_a_players = 11
team_b_players = 11
is_break = False

for index, element_1 in enumerate(a_team_list):

    if element_1 in red_cards_list and index <= 10:
        if element_1 in team_a_red_cards_list:
            continue
        else:
            team_a_red_cards_list.append(element_1)
            team_a_players -= 1
    elif element_1 in red_cards_list and index > 10:
        if element_1 in team_b_red_cards_list:
            continue
        else:
            team_b_red_cards_list.append(element_1)
            team_b_players -= 1

    if team_a_players == 6 or team_b_players == 6:
        is_break = True
        break

print(f"Team A - {team_a_players}; Team B - {team_b_players}")
if is_break:
    print("Game was terminated")
