import random

stake = int(input("enter stake = "))
goal = int(input("enter goal = "))
n = int(input("enter trails = "))
while(n!=0):
    r = random.randint(0,1)  #here generate random integers 
    print(r)
    if r==1:
        stake+=1
        print("stake = {}".format(stake))
        if(stake==goal):
            print("won")
            break
    elif r==0:
        n-=1
        print("n = {}".format(n))
    if(n==0):
        print("lost all chances")