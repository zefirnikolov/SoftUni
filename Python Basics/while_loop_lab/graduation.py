name = input()
grade = 1
bad_scores_counter = 0
scores_sum = 0

is_graduated = True

while grade <= 12:
    current_score = float(input())

    if current_score < 4:
        bad_scores_counter += 1
        if bad_scores_counter == 2:
            is_graduated = False
            break
        continue

    grade += 1
    scores_sum += current_score

if is_graduated:
    print(f"{name} graduated. Average grade: {(scores_sum / 12):.2f}")

else:
    print(f"{name} has been excluded at {grade} grade")
