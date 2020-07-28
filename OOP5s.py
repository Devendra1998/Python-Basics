# ************class method as alternative Constructor*********
class Employee:
    no_of_leaves = 8


    def __init__(self,aname,asalary,arole):
        self.aname= aname
        self.asalary=asalary
        self.arole=arole
    def print_detail(self):
        return f"Name is {self.name},salary is {self.salary},and role is {self.role}"

    @classmethod
    def change_no_of_leaves(cls,new_leaves):
        cls.no_of_leaves = new_leaves

    @classmethod
    def from_str(cls,string):
        return cls(*string.split("-"))
       # param = string.split("-")
       # print(param)
       # return cls(param[0],param[1],param[2])


tanay = Employee("Tanay",6996575,"athlete")
monu  = Employee("Madanmohan",675686976,"Farmer")
karan = Employee.from_str("karan-500-Teacher")
print(karan.asalary)

# tanay.change_no_of_leaves(50)
# print(monu.no_of_leaves)




