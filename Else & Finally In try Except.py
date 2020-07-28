f1= open("deva.txt")

try:
    f=open("does.txt")

except Exception as e:

    print(e)
    print("Important stuff")

else:
    print("THis will run only if except is not running ")

finally:
    print("Run this anyway...")
    #f.close()
    f1.close()