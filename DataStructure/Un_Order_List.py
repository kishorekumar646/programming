from Utility import utility



try:
    
    file_list = open("Un_Order_Lista_Data.txt","r+").read().split(" ")
    
    linked_list = utility.LinkedList()
    for word in file_list:
        linked_list.add(word)
    
    linked_list.dispalyList()
    
    linked_list.pop()
    linked_list.dispalyList()

    linked_list.pop()
    linked_list.dispalyList()

except FileNotFoundError:
    
    print("Error")