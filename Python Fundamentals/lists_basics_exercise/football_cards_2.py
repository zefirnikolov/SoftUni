cards_notebook = input()

a_team_list = ["A-1", 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
b_team_list = ["B-1", 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
red_cards_list = cards_notebook.split()

is_game_terminated = False

for player_eq_element in red_cards_list:
    if player_eq_element in a_team_list:
        a_team_list.remove(player_eq_element)
    elif player_eq_element in b_team_list:
        b_team_list.remove(player_eq_element)

    if len(a_team_list) < 7 or len(b_team_list) < 7:
        is_game_terminated = True
        break

print(f"Team A - {len(a_team_list)}; Team B - {len(b_team_list)}")
if is_game_terminated:
    print("Game was terminated")
