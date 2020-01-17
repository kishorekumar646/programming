import math

"""   Desc  -> Computes the prime factorization of N using brute force.
      I/P   -> Number to find the prime factors
      Logic -> Traverse till i*i <= N instead of i <= N for efficiency.
      O/P   -> Print the prime factors of number N.                """


def printing_primeFactorsNumbers(num):
    print("Prime Factors are : ",end="")
    while (num%2) == 0:
        print(2,end=" ")
        num //=2
    for check_prime_number in range(3,int(math.sqrt(num))+1,2):
        while (num%check_prime_number) == 0:
            print(check_prime_number,end=" ")
            num //=check_prime_number
    if num>2:
        print(num,end="")

try:
    taking_input = int(input("Enter the number : "))
    printing_primeFactorsNumbers(taking_input)
    print()
except ValueError:
    print("Input should be an Integer ! ")