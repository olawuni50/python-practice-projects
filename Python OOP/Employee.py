class Employee:
    """ parent class"""
    def __init__(self, name, salary = 0):
        self.name = name
        self.salary = salary

    def giveRaise(self, percent):
        self.salary = self.salary + (self.salary * percent)
        return f"{self.name} Salary: {self.salary}"

    def work(self):
        return self.name, "does stuff"

    def __repr__(self):
        return "Employee name: %s\nSalary: %s" % (self.name, self.salary)


class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 5000)

    def work(self):
        return self.name, "cooks food"

class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 3000)

    def work(self):
        return self.name, "serves food to customers"

class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)

    def work(self):
        return self.name, "makes pizza"


if __name__ =="__main__":

    for klass in PizzaRobot, Chef, Server, PizzaRobot:
        obj = klass(klass.__name__)
        print(obj.work())
        print(obj.giveRaise(0.2))
        print(obj)

