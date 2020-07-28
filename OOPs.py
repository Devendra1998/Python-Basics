# classes -  Templet
# Object- Intance of the class

# DRY - Do not repeat yourself

#
# class student :
#     pass
#
# dev=student()
# larry=student()
# dev.name="dev"
# dev.std= 12
# dev.section= 1
# larry.name="larry"
# larry.subject=["Networking","Data mining"]
# print(dev.name,larry.subject)

class Employee:
    no_of_leaves = 8
    pass

dev = Employee()
harry= Employee()

dev.name="dev"
dev.salary=86769
dev.role ="Instructor"

harry.name ="rohan"
harry.salary=78647
harry.role="student"
print(Employee.no_of_leaves)
print(dev.__dict__)
Employee.no_of_leaves=9
print(Employee.__dict__)