import random

def print_distinct_couponNumbers(num,c,m,a):
    while (m!=num):
        x = random.randint(0,num)
        c+=1
        if x not in a:
            a.append(x)
            m+=1
    print("Distinct Coupon List : ",a)
    print("Iteration for to print the Coupon numbers : ",c)

try:
    couponList = []
    iteration_count = 0
    couponNumbersCount = 0
    distinct_couponNumber_Count = int(input("enter num = "))
    print_distinct_couponNumbers(distinct_couponNumber_Count,iteration_count,couponNumbersCount,couponList)
except ValueError:
    print("Enter Integers only ! ")