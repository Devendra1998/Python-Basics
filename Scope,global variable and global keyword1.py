l= 10 # Global

def function1(n):
     # l=5 #local
     m=8 #local
     global l
     l= l+ 45
     print(l,m)
     print(n,"I have printed")

function1("This is me")
# print(l)

# in python global variable is read only variable.
# pthon does not allow easily to change the value of gloal variable.
# if we wnant to chnge the value of global variable then we have to use global keyword.
x=90
def dev():
    x=20
    def monu():
        global x
        x=50
    # print("before calling monu",x)
    monu()
    print("after calling monu",x)

dev()
print(x)