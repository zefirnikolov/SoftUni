from Fundamentals.objects_and_classes.child_class import Child


class GrandChild(Child):
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address

    def get_address(self):
        return self.address


test = GrandChild('Ivan', 16, 'Sofia')
print(test.name, test.age, test.address)
