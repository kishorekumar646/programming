stake = int(input("enter stake = "))
goal = int(input("enter goal = "))
trails = int(input("enter trails = "))

bc = 1
n=50
og = goal
wc = 0

while(n==1):
    if(bc == goal):
        print("won")
        goal = goal+og
        wc = wc+1
        n = n-1
    else:
        stake = int(input("enter stake again = "))
        bc = stake
   

print("wc={}".format(wc))
print("bc={}".format(bc))
#print("per={}".format(per))

