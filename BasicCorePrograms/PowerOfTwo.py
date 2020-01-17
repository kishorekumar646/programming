"""   Desc  -> This program takes a command-line argument N and prints a table of the powers
               of 2 that are less than or equal to 2^N.
      I/P   -> The Power Value N. Only works if 0 <= N < 31 since 2^31 overflows an int
      Logic -> repeat until i equals N.
      O/P   -> Print the power of 2 table.           """

try:
    term = int(input("Enter the number : "))

    # lambda arguments : Expression , map(fun,iter)
    result = list(map(lambda x:2 ** x,range(term)))
    for i in range(term):
        print("2 power of ",i," is : ",result[i])
except ValueError:
    print("Input wrong!")