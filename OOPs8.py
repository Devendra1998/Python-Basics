# *********************** Multiple Inheritance**************************
class Employee:
    var=8
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

class Player:
    var=9
    no_of_games=4
    def __init__(self,name,game):
        self.name = name
        self.game = game

    def printdetail(self):
        return f"The name is {self.name}. game is {self.game}"

class coolprogrammer(Employee,Player):
    var=10
    language = "C++"
    def printlanguage(self):
        print(self.language)


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")

shubham = Player("Shubham",["Cricket"])
karan = coolprogrammer("Karan",47657,"coolprogrammer")
karan.printlanguage()