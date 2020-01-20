from Utility import utility


try:

    file_list = open("Order_List_Data.txt","r+").read().split(" ")
    
    linked_list = utility.LinkedList()
    for digit in file_list:
        linked_list.add(digit)

    linked_list.dispalyList()
    linked_list.pop()
    linked_list.dispalyList()

except FileNotFoundError:

    print("File Not Found")