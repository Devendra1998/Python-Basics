class Employee:
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):
        self.aname= aname
        self.asalary=asalary
        self.arole=arole
    def print_detail(self):
        return f"Name is {self.name},salary is {self.salary},and role is {self.role}"

tanay = Employee("Tanay",6996575,"athlete")
print(tanay.aname)
# dev = Employee()
# harry= Employee()
#
# dev.name="dev"
# dev.salary=86769
# dev.role ="Instructor"
#
# harry.name ="harry"
# harry.salary=78647
# harry.role="student"
#
# print(harry.print_detail())




