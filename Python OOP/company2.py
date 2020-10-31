""" Engineering Department
"""
from company1 import Manager, Accountant, Admin
class CTO(Admin):
    def __init__(self, fname, lname, age, position):
        Admin.__init__(self, fname, lname, age, position, 8000)

    def order(self, manager):
        return self.position, " receives orders from ", manager

    def salary_payment(self, accountant):
        return self.position, "receives salary from ", accountant


class COO(CTO):
    def __init__(self, fname, lname, age, position):
        CTO.__init__(self, fname, lname, age, position)

    def order(self, CTO):
        return self.position, " gives report to ", CTO

class Company:
    def __init__(self):
        self.manager = Manager("Dele", "Ben", 39, "Manager")
        self.accountant = Accountant("Perry", "Jones", 59, "Accountant", 10000000)
        self.staff = COO("Tyler", "Jones", 23, "COO")

    def all(self):
        cto = CTO("Peter", "Jack", 67, "CTO")
        coo = COO("Kyle", "Daniel", 43, "COO")
        print(coo.order(self.manager))
        print(coo.salary_payment(self.accountant))
        print(coo.total_salary())
        print(coo)
        print(cto.order(self.manager))
        print(cto.salary_payment(self.accountant))
        print(cto.retirement_age())
        print(cto.total_salary())
        print(cto)

if __name__ == "__main__":
    company = Company()
    company.all()


