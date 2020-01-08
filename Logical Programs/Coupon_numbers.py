import random
def find(num,c,m,a):
    while (m!=num):
        x = random.randint(0,num)
        c+=1
        if x not in a:
            a.append(x)
            m+=1
    print(a)
    print(c)

a = []
c=0
m=0
num = int(input("enter num = "))
find(num,c,m,a)