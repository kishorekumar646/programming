"""
    Read in a list of words from File. Then prompt the user to enter a word to search the list. 
    The program reports if the search word is found in the list.

"""

def BinarySearch(arr,search):

    big,end = 0,len(arr)-1
    arr.sort()
    
    while big <= end:
    
        mid = (big+end) // 2
        
        if arr[mid] == search:
            return True
        
        elif arr[mid] < search:
            big = mid + 1
        
        else:
            end = mid - 1
    
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