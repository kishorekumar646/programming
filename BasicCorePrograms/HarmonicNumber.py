"""  Desc  -> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N (http://users.encs.concordia.ca/~chvatal/notes/harmonic.html).
     I/P   -> The Harmonic Value N. Ensure N != 0
     Logic -> compute 1/1 + 1/2 + 1/3 + ... + 1/N
     O/P   -> Print the Nth Harmonic Value.            """

try:
    taking_input = int(input("Enter the number : "))
    harmonic_sum = 0
    for series in range(1,taking_input+1):

        #(1/1)+(1/2)+(1/3)+(1/4)+.............+(1/n)
        harmonic_sum += 1/series
    print("Nth Harmonic value is : ",round(harmonic_sum,3))
except ValueError:
    print("\nIt should be an Integer ! \n")