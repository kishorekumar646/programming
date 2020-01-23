import file_system
import address_book
import json

def add():
    global id_number
    with open("data.json",'r') as data:
        s = json.load(data)
        for d in s["persons"]:
            id_number += 1                     
                        
    print("\n\t--------- Enter your details here  ----------\n")
    
    first_name = str(input("Enter first name : "))
    last_name = str(input("Enter last name : "))
    address = str(input("Enter address : "))
    city = str(input("Enter city : "))
    state = str(input("Enter state : "))
    zip_code = str(input("Enter zip : "))
    phone_number = str(input("Enter phone number : "))
    
    h = address_book_object.addPerson(id_number,first_name,last_name,address,city,state,zip_code,phone_number)
    data = file_system_object.readFile("data.json")
    
    data["persons"].append(h)
    
    file_system_object.saveFile(data,"data.json")

def update():

    try:

        data = file_system_object.readFile("data.json")

        for index_val in range(len(data["persons"])):
            print(index_val,end=" ")
        print()

        update_index = int(input("which index do you want to update : "))
        address = str(input("Enter address : "))
        city = str(input("Enter city : "))
        state = str(input("Enter state : "))
        zip_code = str(input("Enter zip : "))
        phone_number = str(input("Enter phone number : "))

        flag = 0

        for d in data["persons"]:
            if d["id"] == update_index:
                d["address"] = address
                d["city"] = city
                d["state"] = state
                d["zip"] = zip_code
                d["phone_number"] = phone_number
                flag = 1
        
        if flag == 0:
            raise IndexError

        file_system_object.saveFile(data,"data.json")

    except IndexError:
        print("\nwrong index")

def delete():

    data = file_system_object.readFile("data.json")

    try:

        for index_val in range(len(data["persons"])):
            print(index_val,end=" ")
        print()

        del_index = int(input("which index do you want to delete : "))

        del data["persons"][del_index]
        
        file_system_object.saveFile(data,"data.json")

    except IndexError:
        
        print("wrong index")

if __name__ == "__main__":

    try:
    
        file_system_object = file_system.FileSystem()
        address_book_object = address_book.AddressBook()

        id_number = 0
        b = True
        while b:
            print("\n1.Open address book\t2.Create adress book\t3.Quit application\n")
            choice = int(input("Enter your choice : "))
            
            if choice == 1:
                

                print("\n1.Add\t2.update\t3.delete\n")
                choice1 = int(input("Enter your choice : "))
                    
                def number(ar):
                    switcher = {
                        1 : add,
                        2 : update,
                        3 : delete,
                    }
                    return switcher.get(ar,lambda : "Wrong input please try again!")

                s = number(choice1)
                s()   

            elif choice == 2:
                pass

            elif choice == 3:
                b = False
                print("\n\t---------- stored data  ----------\n")
            
            else:
                print("Wrong input!")

    except ValueError:
        print("\n\t-----------  Take integers only  ----------\n")
