# ***********Public,Protected and Private Access specifier**************
# Here in python default access specifier is Public

class Employee:
    var=8
    no_of_leaves = 8
    _protec=5
    __private=9

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

dev=Employee("Dev",563363,"Developer")
print(dev._Employee__private)

# Python use its own namingly for accessing private variable