import time


initial = time.time()
k=0
while(k<50):
    print("I am Dev")
    time.sleep(1)
    k+=1
print("while loop time is",time.time(),"Seconds")

initial2=time.time()
for i in range(50):
    print("I am Dev")
print("for loop time is", time.time() , "Seconds")