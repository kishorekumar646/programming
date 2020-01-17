def BinarySearch(arr,search):
    big,end = 0,len(arr)-1
    arr.sort()
    #print(arr)
    while big <= end:
        mid = (big+end) // 2
        if arr[mid] == search:
            return True
        elif arr[mid] < search:
            big = mid + 1
        else:
            end = mid - 1
    return False

f = open("Data.txt","r").read().split(" ")
lst = []
for i in f:
    lst.append(i)
    lst.
print(lst)
s = str(input("Enter search name : "))
if BinarySearch(lst,s):
    print("FOUND")
else:
    print("NOT FOUND")
f.clear()