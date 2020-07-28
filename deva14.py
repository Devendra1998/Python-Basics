num1=input("enter a number")
num2=input("enter a number")
try:
    print("sum of these numbers ",int(num1)+int(num2))
except Exception as e:
    print(e)
    print("this mut be print")
