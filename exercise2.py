#Exercise 2 - Faulty calculater
print("Enter 1st number")
num1=int(input())
print("Enter 2nd number")
num2=int(input())
print("so what you want?+<,-,*,/")
num3=input()

if num1==45 and num2==3 and num3=='*':
    print("154")
elif num1==56 and num2==9 and num3=='+':
    print("77")
elif num1==56 and num2==6 and num3=='/':
    print("4")
elif num3=='*':
    num4=num1+num2
    print(num4)
elif num3=='+':
    num5=num1+num2
    print(num5)
elif num3=='/':
    num6=num1/num2
    print(num6)
elif  num3=='-':
 num7=num1-num2
 print(num7)
