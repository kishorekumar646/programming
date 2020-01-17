def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while (j>=0 and arr[j] > key):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
    print(arr)

try:
    size = int(input("Enter the array size : "))
    list_array = [str(input()) for i in range(size)]
    insertionSort(list_array)
except ValueError:
    print("Wrong Input")