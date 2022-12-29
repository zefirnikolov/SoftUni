def password_validator(inp):
    is_valid = True
    if len(inp) < 6 or len(inp) > 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not inp.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False
    digits_counter = 0
    for ch in inp:
        if ch.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    return is_valid


some_password = input()
is_validated = password_validator(some_password)
if is_validated:
    print("Password is valid")
