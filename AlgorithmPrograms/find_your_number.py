n = int(input("enter a number[0-9]:"))
N = 2**n
my_list=[i for i in range(0,N-1)]
low = 0
high = len(my_list)-1
def number(n,my_list,low,high):
    mid = low+(high-low)//2
    Found = False
    while low<=high and not Found: 
        if n == my_list[mid]:
            return my_list[mid]
            Found = True
        elif n>my_list[mid]:
            return number(n,my_list,mid+1,high)
        else:
            return number(n,my_list,low,mid-1)
print("entered number is:",number(n,my_list,low,high))