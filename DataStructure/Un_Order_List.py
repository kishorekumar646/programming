from Utility import utility

try:
    
    file_list = open("Un_Order_List_Data.txt","r+").read().split(" ")
    
    linked_list = utility.LinkedList()
    for word in file_list:
        linked_list.add(word)
    
    print("1.Insert\t2.Display List\t3.Search Item\t4.Delete\t5.Terminate")
    b = True
    while b:
        choice = int(input("Enter your choice : "))
        if choice == 1:
            
            f = open("Un_Order_List_Data.txt","a")
            item = str(input("Enter the name : "))
            linked_list.append(item)
            f.write(" "+item)
            f.close()

        elif choice == 2:
            
            linked_list.dispalyList()

        elif choice == 3:
            
            item = str(input("Enter the search name : "))
            
            if linked_list.search(item):

                print("Found")
                f = open("Un_Order_List_Data.txt","r")
                l = f.read().split(" ")
                f.close()
                print(l)

                linked_list.delete(item)
                
                lst = []
                for words in l:
                    
                    if words == item:
                        continue
                    
                    else:
                        lst.append(words)

                s = ' '.join(lst)
                f = open("Un_Order_List_Data.txt","w")
                f.write(s)
                f.close()
                print(item," Deleted in list")
            
            else:
                f = open("Un_Order_List_Data.txt","a")
                
                print("Not Found")
                
                linked_list.append(item)
                
                f.write(" "+item)
                
                print(item," Added in list")
        
                f.close()
        elif choice == 4:

            linked_list.pop()

        elif choice == 5:
            b = False
            

        else:
            print("Wrong Input")

except FileNotFoundError:
    
    print("File Not Found")