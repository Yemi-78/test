class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + 'nibss-plc.com.ng'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp1 = Employee("Yemi", "Ala", 5000)
print(emp1.fullname())