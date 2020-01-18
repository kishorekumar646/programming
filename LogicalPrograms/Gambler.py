import random

"""
    Simulates a gambler who start with $stake and place fair $1 bets until he/she goes broke (i.e. has no money) or 
    reach $goal. Keeps track of the number of times he/she wins and the number of bets he/she makes. 
    Run the experiment N times, averages the results, and prints them out.
"""
try:

    stake = int(input("enter stake = "))
    goal = int(input("enter goal = "))
    trails = int(input("enter trails = "))

    while(trails!=0):

        random_number = random.randint(0,1)
        print(random_number)

        if random_number==1:
            stake+=1
            print("stake = {}".format(stake))
            if(stake==goal):
                print("won")
                break

        elif random_number==0:
            trails-=1
            print("trails = {}".format(trails))

        if(trails==0):
            print("lost all chances")

except ValueError:
    print("Error")