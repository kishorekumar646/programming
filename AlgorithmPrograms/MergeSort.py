"""

    a program to do Merge Sort of list of Strings. 

"""

def mergeSort(array_list):

    if len(array_list) > 1:
        
        mid_value = len(array_list) // 2
        left = array_list[:mid_value]
        right = array_list[mid_value:]

        mergeSort(left)
        mergeSort(right)

        left_halves = right_halves = merge_halves = 0

        while left_halves < len(left) and right_halves < len(right):
            
            if left[left_halves] < right[right_halves]:
                array_list[merge_halves] = left[left_halves]
                left_halves += 1
            
            else:
                array_list[merge_halves] = right[right_halves]
                right_halves += 1
            
            merge_halves +=1

        while left_halves < len(left):
            
            array_list[merge_halves] = left[left_halves]
            left_halves += 1
            merge_halves += 1
        
        while right_halves < len(right):
            
            array_list[merge_halves] = right[right_halves]
            right_halves += 1
            merge_halves += 1
    
    print(array_list,end="")


try:

    list_size = int(input("Enter the size of lisr : "))
    
    data_list = [str(input()) for take_list in range(list_size)]
    
    print(data_list)
    
    mergeSort(data_list)
    print()

except ValueError:

    print("Error")