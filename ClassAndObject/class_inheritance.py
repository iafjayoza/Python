# Class example by inheritance

class employee:

    raise_amt = 1.03

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return "{} {}".format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class developer(employee):
    raise_amt = 1.05

    def __init__(self,first,last,pay,pro_lang):
        super().__init__(first,last,pay)
        self.pro_lang = pro_lang

class manager(employee):

    def __init__(self,first,last,pay,employees = None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print(emp.fullname())


emp1 = developer("Jay","Oza",1800000,"Python")
emp2 = developer("Ashu","Sinha",1900000,"Java")

# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)
# print(emp1.pro_lang)

mgr_1 = manager("Rahul","Rakholiya",2100000,[emp1])

mgr_1.add_emp(emp2)
mgr_1.remove_emp(emp1)
mgr_1.print_emp()

# (print(isinstance(mgr_1,manager)))
# (print(isinstance(mgr_1,employee)))
# (print(isinstance(mgr_1,developer)))

# (print(issubclass(developer,employee)))
# (print(issubclass(developer,developer)))
# (print(issubclass(developer,manager)))


