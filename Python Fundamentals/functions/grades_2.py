def type_of_grade(current_grade):
    result = ''
    if 2 <= current_grade <= 2.99:
        result = "Fail"
    elif 3 <= current_grade <= 3.49:
        result = "Poor"
    elif 3.5 <= current_grade <= 4.49:
        result = "Good"
    elif 4.5 <= current_grade <= 5.49:
        result = "Very Good"
    elif 5.5 <= current_grade <= 6:
        result = "Excellent"
    return result


grade_data = float(input())

print(type_of_grade(grade_data))
