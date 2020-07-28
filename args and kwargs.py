# def print_name(a,b,c,d):
#     print(a,b,c,d)
#
#
# print_name("dev","monu","tanaya","laxmi")

# In this convention if want to add another name then we have
# to add another argument.hence it become quite tedious for
# large users .here we taking the advantages of python function


def funargs(normal,*args,**kwargs):
    print(normal)
    for item in args:
        print(item)
    print("Now i would like to introduced some of our heroes")
    for key,value in kwargs.items():
        print(f"{key} is a {value}")


har=["Dev","Monu","himanshu","anuj","tanaya"]
a="I am normal student and rest normal student"
kw={"Dev":"student","monu":"Farmer","Tanay":"School Boy"}
funargs(a,*har,**kw)

# in args it is not necessary that we will name the argument of
# function as args.we can name it anything that best suited
# in above example normal will be there as first argument
# after that any no of argument there
# in last we are forced  use *args argument otherwise it throw error
# in args function data is processed as tuple whether it tuple or list
# no we seeing the about the args
# args and kwargs are optional

