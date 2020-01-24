from file_system import FileSystem
from address_book import AddressBook
from person import Person
import json


file_system_object = FileSystem()
address_book_object = AddressBook()

def read_person():
        return {
            'firstname': input("enter firstname:"),
            'lastname': input("enter lastname:"),
            'address': input("enter address:"),
            'city': input("enter city:"),
            'state': input("enter state:"),
            'zipcode': input("enter zipcode:"),
            'phonenumber': input("enter phonemuber:")
        }

def add(address_book_object_call):
    new_person = Person(read_person())

    address_book_object_call.addPerson(new_person)
    
    file_system_object.saveFile("data.json", address_book_object_call)
    

def update():

    # try:

    #     data = file_system_object.readFile("data.json")

    #     for index_val in range(len(data["persons"])):
    #         print(index_val,end=" ")
    #     print()

    #     update_index = int(input("which index do you want to update : "))
    #     address = str(input("Enter address : "))
    #     city = str(input("Enter city : "))
    #     state = str(input("Enter state : "))
    #     zip_code = str(input("Enter zip : "))
    #     phone_number = str(input("Enter phone number : "))

    #     flag = 0

    #     for d in data["persons"]:
    #         if d["id"] == update_index:
    #             d["address"] = address
    #             d["city"] = city
    #             d["state"] = state
    #             d["zip"] = zip_code
    #             d["phone_number"] = phone_number
    #             flag = 1

    #     if flag == 0:
    #         raise IndexError

    #     file_system_object.saveFile(data,"data.json")

    # except IndexError:
    #     print("\nwrong index")
    pass


def delete():

    # data = file_system_object.readFile("data.json")

    # try:

    #     for index_val in range(len(data["persons"])):
    #         print(index_val,end=" ")
    #     print()

    #     del_index = int(input("which index do you want to delete : "))

    #     del data["persons"][del_index]

    #     file_system_object.saveFile(data,"data.json")

    # except IndexError:

    #     print("wrong index")
    pass


def print_data():

    address_book_object.printAll()


if __name__ == "__main__":

    try:


        b = True
        while b:

            address_book_object = file_system_object.readFile("data.json")

            print("\n1.Open address book\t2.Create adress book\t3.Quit application\n")
            choice = int(input("Enter your choice : "))

            if choice == 1:

                print("\n1.Add\t2.update\t3.delete\t4.print_data\n")
                choice1 = int(input("Enter your choice : "))

                def number(ar):
                    switcher = {
                        1: add(address_book_object),
                        2: update(),
                        3: delete(),
                        4: print_data()
                    }
                    return switcher.get(ar, lambda: "Wrong input please try again!")

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
