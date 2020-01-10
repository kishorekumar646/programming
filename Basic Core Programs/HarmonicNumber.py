try:
    taking_input = int(input("Enter the number : "))
    harmoni_sum = 0
    for i in range(1,taking_input+1):
        harmoni_sum += 1/i       #(1/1)+(1/2)+(1/3)+(1/4)+.............+(1/n)
    print("Nth Harmonic value is : ",round(harmoni_sum,3))
except ValueError:
    print("\nIt should be an Integer ! \n")