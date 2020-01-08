try:
    n = int(input("Enter the number : "))
    sum = 0
    for i in range(1,n+1):
        sum += 1/i
    print("Nth Harmonic value is : ",round(sum,3))
except ValueError:
    print("Input wrong!")