class Employee {
    constructor(name, salary = 0) {
        this.name = name
        this.salary = salary
    }
    giveRaise(percent) {
        this.salary = this.salary + (this.salary * percent)
        return `Salary increase: ${this.salary}`
    }
    work() {
        return `${this.name} does stuff`
    }
    describe() {
        return `Employee Name: ${this.name}, Salary: ${this.salary}`
    }
}

class Chef extends Employee {
    constructor(name) {
        super(name, 5000)
    }
    work() {
        return `${this.name} cooks food`
    }
}
class Server extends Employee {
    constructor(name) {
        super(name, 4000)
    }
    work() {
        return `${this.name} serves food`
    }
}
class PizzaRobot extends Chef {
    constructor(name) {
        super(name)
    }
    work() {
        return `${this.name} assist chef`
    }
}

let chef = new Chef("John")
let server = new Server("Bob")
console.log(chef.work())
console.log(chef.giveRaise(0.2))
console.log(chef.describe())
console.log(server.work())