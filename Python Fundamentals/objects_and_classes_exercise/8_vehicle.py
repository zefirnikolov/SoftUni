class Vehicle:
    def __init__(self, type_of_vehicle, model, price, owner=None):
        self.type_of_vehicle = type_of_vehicle
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, money: int, owner: str):
        if money >= self.price and self.owner is None:
            self.owner = owner
            change = money - self.price  # possible pitfall - float - change
            return f"Successfully bought a {self.type_of_vehicle}. Change: {change:.2f}"
        if money < self.price and self.owner is not None:
            return f"Sorry, not enough money\nCar already sold"
        if money < self.price:
            return f"Sorry, not enough money"
        elif self.owner is not None:  # Possible Pitfall - maybe only 1 condition needed 1st.
            return f"Car already sold"

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.type_of_vehicle} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type_of_vehicle} is on sale: {self.price}"


# vehicle_type = "car"
# model = "BMW"
# price = 30000
# vehicle = Vehicle(vehicle_type, model, price)
# print(vehicle.buy(15000, "Peter"))
# print(vehicle.buy(35000, "George"))
# print(vehicle)
# vehicle.sell()
# print(vehicle)
