try:
    term = int(input("Enter the number : "))
    result = list(map(lambda x:2 ** x,range(term)))   # lambda arguments : Expression , map(fun,iter)
    for i in range(term):
        print("2 power of ",i," is : ",result[i])
except ValueError:
    print("Input wrong!")