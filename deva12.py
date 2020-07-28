#operators
lower=int(input("enter lower number"))
upper=int(input("enter upper number"))
for num in range(lower,upper+1):
    prime=True
    if num>1:
     for i in range (2,num):
            if( num % i == 0):
                prime=False
    if prime==True:
                print("prime numbers are",num)