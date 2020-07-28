#f=open("devapandey.txt","w")
#a=f.write("deva you are a good boy\n")
#print(a)
#f.close()

#f=open("devapandey2.txt","a")
#a=f.write("deva you are a good boy\n")
#print(a)
#f.close()

#handle read and write both
f=open("devapandey2.txt","r+")
print(f.read())
f.write("thankyou")