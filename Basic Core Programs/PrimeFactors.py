import math

def printing_primeFactorsNumbers(num):
    print("Prime Factors are : ",end="")
    while (num%2) == 0:
        print(2,end=" ")
        num //=2
    for i in range(3,int(math.sqrt(num))+1,2):
        while (num%i) == 0:
            print(i,end=" ")
            num //=i
    if num>2:
        print(num,end="")

try:
    taking_input = int(input("Enter the number : "))
    printing_primeFactorsNumbers(taking_input)
    print()
except ValueError:
    print("Input should be an Integer ! ")