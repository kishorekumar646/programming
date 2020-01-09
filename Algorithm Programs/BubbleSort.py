def BubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)

n = int(input("Enter the size of array : "))
lst = [int(input()) for i in range(n)]
print(lst)
BubbleSort(lst)