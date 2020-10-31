""" Administration Department
"""


class Admin:
    def __init__(self, fname, lname, age, position, salary):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.position = position
        self.salary = salary

    def role(self):
        return self.position, "does stuff"

    def retirement_age(self):
        if self.age >= 70:
             return f"At {self.age} you should retire"
        else:
            return f"At {self.age}, you are still fit to work"

    def monthly_salary_bonus(self):
        """Admin department receives 10% bonus every month"""
        print("\nMonthly salary with Bonus")
        return ((self.salary * 0.1) + self.salary)

    def tax_insurance_deduction(self):
        """deduction of 20% monthly on tax and  insurance"""
        print("Monthly Tax and Insurance deduction: ")
        return self.salary * 0.2

    def total_salary(self):
        """print total salary of staff"""
        print("\nTotal Salary at the end of the month after all bonuses and deductions have been made: ")
        self.salary =((self.salary * 0.1) + self.salary) - (self.salary * 0.2)
        return self.salary

    def __repr__(self):
        return 'Name: %s %s, \nPosition: %s, \nInitials: %s.%s \nSalary: %s' %(self.fname,self.lname, self.position,
                                                                              self.fname[0],self.lname[0], self.salary)


class CEO(Admin):
    def __init__(self, fname, lname, age, position):
        Admin.__init__(self, fname, lname, age, position, 90000)

    def role(self):
        return self.position, "Chief Executive Officer and founder of the company"


class Manager(Admin):

    def __init__(self, fname, lname, age, position):
        Admin.__init__(self, fname, lname, age, position, 70000)

    def role(self):
        return self.fname, "\n1)Manages the affair of the company \n2 Second in command"


class AssManager(Manager):
    """manager and assistant manager receives the same salary"""
    def __init__(self, fname, lname, age, position):
        Manager.__init__(self, fname, lname, age, position)

    def role(self):
        return self.fname, "Assist manager in managing the company"


class Accountant(Admin):
    def __init__(self, fname, lname, age, position, salary):
        self.commodity_price = []
        self.commodity = []
        self.salary = salary
        self._total_amount_inbank = 10000000
        Admin.__init__(self, fname, lname, age, position, 50000)

    def role(self):
        return self.position, "\n1)Keeps all accounts records, \n2)Report to the CEO or account details"

    def commodity_bought(self):
        """input and return commodity bought and the amount
        to be added to the main balance"""

        while True:
            print("Commodity number " + str(len(self.commodity) + 1) + " Enter space bar to quit")
            commodity = input("Enter Commodity: ")
            if commodity == " ":
                break
            commodity_price = int(input(f"Enter {commodity} amount: "))
            print(f"{commodity.title()} : ${commodity_price}")

            self.commodity.append(commodity)                # Add commodity bought to list
            self.commodity_price.append(commodity_price)    # Add commodity prices to list

        print("\nList of Commodity and price")
        d = [commo for commo in self.commodity]             # List comprehension
        a = [amount for amount in self.commodity_price]     # List comprehension

        f = dict(zip(d, a))                                 # Convert list to dictionary
        print(f)

        print("\nTotal price of commodity bought: ")
        print(f"${sum(self.commodity_price)}")               # total amount of commodity bought

        print(f"\n Total Balance")
        print(f"Total Amount in account - Total amount of commodity bought: ")  #Total Balance
        total_amount = (self._total_amount_inbank - sum(self.commodity_price))
        print(f"${total_amount}")


        if total_amount == 0:
            print("You have no money in your account again ")
        elif total_amount < 0:
            print(f"You are in debt of {total_amount}$")


if __name__ == "__main__":
    ceo = CEO("Tyler", "Perry", 70, "CEO")
    manager = Manager("Dele", "Ben", 39, "Manager")
    accountant = Accountant("Perry", "Jones", 59, "Accountant", 10000000)
    print(ceo.role())
    print(ceo.monthly_salary_bonus())
    print(ceo.tax_insurance_deduction())
    print(ceo.total_salary())
    print(ceo)



