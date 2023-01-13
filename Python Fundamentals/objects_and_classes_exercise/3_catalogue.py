class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        return self.products.append(product_name)

    def get_by_letter(self, first_letter):
        new_list = []
        for index in range(len(self.products)):
            element = self.products[index]
            if first_letter in element[0]:
                new_list.append(element)
        return new_list

    def __repr__(self):
        self.products.sort()
        products_list_in_new_line = '\n'.join(self.products)
        result = f"Items in the {self.name} catalogue:\n" + products_list_in_new_line
        return result


catalogue = Catalogue("Furniture")
catalogue.add_product("Mirror")
catalogue.add_product("Sofa")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
