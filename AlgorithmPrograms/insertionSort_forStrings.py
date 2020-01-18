"""

    Reads in strings and prints them in sorted order using insertion sort.

"""

def insertionSort(array_list):
    
    for index in range(1, len(array_list)):
        
        key = array_list[index]
        position = index-1
        
        while (position >= 0 and array_list[position] > key):
        
            array_list[position+1] = array_list[position]
            position = position-1
        
        array_list[position+1] = key
    
    print(array_list)


try:
    
    list_size = int(input("Enter the array size : "))
    list_array = [str(input()) for take_list in range(list_size)]
    insertionSort(list_array)

except ValueError:

    print("Wrong Input")