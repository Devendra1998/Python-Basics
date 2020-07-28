#f.tell() it gives the location of file pointer
#f.seek() it reset the location of pointer or where to start it to read
with open("devapandey2.txt") as f:
    a=f.readlines()
    print(a)
    f=open("devapandey2.txt","rt")
    a=f.readline()
    print(a)
    f.close()
    #question of the day if my file open or not while i using with keyword
#anwer - yes we can open the or can be read