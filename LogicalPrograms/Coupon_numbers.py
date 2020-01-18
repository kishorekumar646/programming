import random
"""
    Given N distinct Coupon Numbers, how many random numbers do you need to generate distinct coupon number? 
    This program simulates this random process.
"""

def print_distinct_couponNumbers(number_count,random_count,distinct_coupon_count,list_coupon):
    
    while (distinct_coupon_count!=number_count):
        
        x = random.randint(0,number_count)
        random_count += 1
        
        if x not in list_coupon:
            list_coupon.append(x)
            distinct_coupon_count+=1
    
    print("Distinct Coupon List : ",list_coupon)
    print("Iteration for to print the Coupon numbers : ",random_count)


try:

    couponList = []
    iteration_count = 0
    couponNumbersCount = 0
    distinct_couponNumber_Count = int(input("enter num = "))
    print_distinct_couponNumbers(distinct_couponNumber_Count,iteration_count,couponNumbersCount,couponList)

except ValueError:

    print("Enter Integers only ! ")