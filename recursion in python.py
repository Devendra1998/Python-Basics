
number = int(input("enter a number"))
# def factorial_recursive(n):


    # if n==1:
    #     return 1

   # else:
   #      return n*factorial_recursive(n-1)

# print("factorial of a number using recursion",factorial_recursive(number))

def fibonnacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonnacci(n-1)+fibonnacci(n-2)

print("Fibonnacci Sequence",fibonnacci(number))
