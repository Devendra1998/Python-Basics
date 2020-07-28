# # **************************Single level Inheritance************************
# class Employee:
#     no_of_leaves = 8
#
#
#     def __init__(self,aname,asalary,arole):
#         self.aname= aname
#         self.asalary=asalary
#         self.arole=arole
#     def print_detail(self):
#         return f"Name is {self.name},salary is {self.salary},and role is {self.role}"
#
#     @classmethod
#     def change_no_of_leaves(cls,new_leaves):
#         cls.no_of_leaves = new_leaves
#
#     @classmethod
#     def from_str(cls,string):
#         return cls(*string.split("-"))
#
#     @staticmethod
#     def print_good(string):
#         print("This a good program  " + string)
#
#
# class Programmer(Employee):
#     def print_prog(self):
#         return f"The programmers  Name is {self.name}. salary is {self.salary} and role is  {self.role}"
#
#
# tanay = Employee("Tanay",6996575,"athlete")
# monu  = Employee("Madanmohan",675686976,"Farmer")
#
# shubham= Programmer("Shubham",23763874,"Programmer")
# karan = Programmer("karan",7455445,"Programmer")
# print(shubham.print_prog())
class Employee:
    no_of_leaves = 8

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


class Programmer(Employee):
    no_of_holiday = 56
    def __init__(self, aname, asalary, arole, languages):
              self.name = aname
              self.salary = asalary
              self.role = arole
              self.languages = languages


    def printprog(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}.The languages are {self.languages}"



harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")

shubham = Programmer("Shubham", 555, "Programmer", ["python"])
karan = Programmer("Karan", 777, "Programmer", ["python", "Cpp"])
print(karan.printprog())