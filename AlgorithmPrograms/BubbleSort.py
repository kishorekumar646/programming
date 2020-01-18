"""
   
    Reads in integers prints them in sorted order using Bubble Sort

"""

def BubbleSort(array_list):

    for index1 in range(len(array_list)-1):
        for index2 in range(len(array_list)-index1-1):
            if array_list[index2] > array_list[index2+1]:
                array_list[index2],array_list[index2+1] = array_list[index2+1],array_list[index2]
    
    print(array_list)

try:

    list_size = int(input("Enter the size of array : "))
    
    data_list = [int(input()) for take_list in range(list_size)]
    
    print(data_list)
    
    #Method calling
    BubbleSort(data_list)

except ValueError:
    
    print("Input should be an Integer")