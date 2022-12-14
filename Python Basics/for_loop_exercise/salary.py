number_of_loops = int(input())
salary = int(input())

is_salary_0 = False

for _ in range(number_of_loops):
    website_name = input()

    if website_name == 'Facebook':
        salary -= 150
    elif website_name == "Instagram":
        salary -= 100
    elif website_name == "Reddit":
        salary -= 50

    if salary <= 0:
        is_salary_0 = True
        break

if is_salary_0:
    print("You have lost your salary.")

else:
    print(salary)
