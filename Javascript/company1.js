class Company {
    constructor(name, job, salary, stacks) {
        this.name = name
        this.job = job
        this.salary = salary
        this.stacks = stacks
    }
    describe() {
        return `Name:${this.name[0]}\nJob: ${this.job}\nSalary $${this.salary}`
    }
    giveRaise(percent) {
        let salary = this.salary + (this.salary * percent)
        return `Monthly Salary raise is $${salary}`
    }
    initials() {
        return `Initials:${this.name[0][0]}.${this.name[1][0]}`
    }
    emailAddress() {
        return `Email address: ${this.name[1]}@company.com`
    }
    level() {
        if (this.salary >= 50000) {
            return `Senior Staff`
        } else {
            return `Junior Staff`
        }
    }
    stack() {
        for (let i = 0; i < this.stacks.length; i++) {
            return `My stacks are ${this.stacks}`
        }
    }
}

let company = new Company(["Tyler", "Jones"], "Software engineer", 59000, ["Python", "JS", "Reactjs", "Django"])
console.log(company.describe())
console.log(company.giveRaise(0.2))
console.log(company.initials())
console.log(company.emailAddress())
console.log(company.level())
console.log(company.stack())