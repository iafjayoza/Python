# Example of employee class
import datetime

class Employee:

    raise_amount = 1.04
    emp_count = 0

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last +"@company.com"

        Employee.emp_count += 1

    def fullname(self):
        return "{} {}".format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def from_string(cls, emp_str):
        first,last,pay = emp_str.split("-")
        return cls(first,last,pay)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @staticmethod
    def is_workday(day):
        return (not(day.weekday() == 5 or day.weekday() == 6))

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


print("Number of employees are", Employee.emp_count)
emp1 = Employee("Jay","Oza",1800000)
emp2 = Employee("Test","User",2100000)
print("Number of employees are", Employee.emp_count)

# print(emp1.first,emp1.last,emp1.email,emp1.pay,emp1.fullname())
# print(emp2.first,emp2.last,emp2.email,emp2.pay,emp2.fullname())
#
# emp1.raise_amount = 1.05
# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)
#
# Employee.set_raise_amount(1.08)
# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)

emp_str1 = "Parth-Jadvani-700000"
emp_str2 = "Ashu-Sinha-900000"

new_emp1 = Employee.from_string(emp_str1)
new_emp2 = Employee.from_string(emp_str2)

(print(new_emp1.first))
(print(new_emp2.first))

mydate = datetime.date(2020,5,22)

(print(Employee.is_workday(mydate)))

print(emp1 + emp2)
print(len(emp1))






