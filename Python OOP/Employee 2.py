from Employee import Server, PizzaRobot


class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(f"{self.name} orders food from {server}")

    def pay(self, server):
        print(f"{self.name} pays money to {server}")


class Oven:
    def bake(self):
        print("bakes food")


class PizzaShop:
    def __init__(self):
        self.server = Server("Bob")
        self.chef = PizzaRobot("Jones")
        self.oven = Oven()

    def order(self):
        customer = Customer("Ben")
        customer.order(self.server)
        customer.pay(self.server)
        self.chef.work()
        self.server.work()


if __name__ == "__main__":
    shop = PizzaShop()
    shop.order()