products_list = input().split()


searching_items = input().split()

for item in searching_items:

    if item in products_list:

        for index in range(len(products_list)):
            element = products_list[index]

            if item == element:
                print(f"We have {products_list[index + 1]} of {element} left")
                break
    else:
        print(f"Sorry, we don't have {item}")
