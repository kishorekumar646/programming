"""
    Read in a list of words from File. Then prompt the user to enter a word to search the list. 
    The program reports if the search word is found in the list.

"""

def BinarySearch(array_list,search_name):

    start,end = 0,len(array_list)-1
    array_list.sort()
    
    while start <= end:
    
        mid_value = (start+end) // 2
        
        if array_list[mid_value] == search_name:
            return True
        
        elif array_list[mid_value] < search_name:
            start = mid_value + 1
        
        else:
            end = mid_value - 1
    
    return False

try:

    #open the file and split into the spaces
    file_list = open("Data.txt","r").read().split(" ")
    
    data_list = []

    for take_list in file_list:
        data_list.append(take_list)
    
    print(data_list)
    input_name = str(input("Enter search name : "))
    
    #calling to method and return the True or False
    if BinarySearch(data_list,input_name):
        print("FOUND")
    
    else:
        print("NOT FOUND")
    
    #close the file
    file_list.clear()

except FileNotFoundError:
    
    print("File Not Exist")