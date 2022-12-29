def password_checker(inp):
    len_inp = len(inp)
    is_between_6_10 = False
    is_digit_or_letter = True
    is_at_least_2_digits = False
    if 6 <= len_inp <= 10:
        is_between_6_10 = True
    int_counter = 0
    for ch in inp:
        if ch.isdigit():
            int_counter += 1

        if 65 <= ord(ch) <= 90 or 97 <= ord(ch) <= 122 or ch.isdigit():
            continue
        else:
            is_digit_or_letter = False
    if 2 <= int_counter <= len(inp):
        is_at_least_2_digits = True
    if is_between_6_10 and is_digit_or_letter and is_at_least_2_digits:
        return f"Password is valid"
    elif is_between_6_10 == False and is_digit_or_letter and is_at_least_2_digits:
        return f"Password must be between 6 and 10 characters"
    elif is_between_6_10 == False and is_digit_or_letter == False and is_at_least_2_digits:
        return f"Password must be between 6 and 10 characters\nPassword must consist only of letters and digits"
    elif is_between_6_10 == False and is_digit_or_letter == False and is_at_least_2_digits == False:
        return f"Password must be between 6 and 10 characters\n" \
               f"Password must consist only of letters and digits\nPassword must have at least 2 digits"
    elif is_between_6_10 and is_digit_or_letter == False and is_at_least_2_digits:
        return f"Password must consist only of letters and digits"
    elif is_between_6_10 and is_digit_or_letter == False and is_at_least_2_digits == False:
        return f"Password must consist only of letters and digits\nPassword must have at least 2 digits"
    elif is_between_6_10 and is_digit_or_letter and is_at_least_2_digits == False:
        return f"Password must have at least 2 digits"


password = input()
print(password_checker(password))

# True True True
# False True True
# False False True
# False False False
# True False True
# True False False
# True True False
