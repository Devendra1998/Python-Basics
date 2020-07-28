# There is advice minimize the use multiole inheritance becuse it create
# problems like ambiguity in method call etc.
# Example of Diamond shape problem.it arises due to use of
# Multiplr inheritance.So,better to avoid it.
class A:
    def met(self):
        print("This is a method from class A")

class B(A):
    def met(self):
        print("This is a Method from class B")

class C(A):
    def met(self):
        print("This is a method from class C")

class D(B,C):
    def met(self):
        print("This is a method from class D")


a=A()
b=B()
c=C()
d=D()
d.met()