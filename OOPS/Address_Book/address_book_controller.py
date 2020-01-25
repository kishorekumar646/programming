from file_system import FileSystem
from address_book import AddressBook
from person import Person


class AddressBookController:

    def __init__(self):
        self.address_book_object = AddressBook()
        self.create_address_book_object = AddressBook()
        self.file_system_object = FileSystem()

    def open_address_book(self):

        self.address_book_object = self.file_system_object.readFile(
            "data.json")
        print("\n1.Add\t2.update\t3.delete\t4.print_data\n")
        choice1 = int(input("Enter your choice : "))
        if choice1 == 1:

            self.add(self.address_book_object, self.file_system_object)
            print("\n\t-------  successfully added  --------\n")

        elif choice1 == 2:
            pass

        elif choice1 == 3:
            index = int(input("Enter index number : "))
            self.address_book_object.removePerson(index)
            self.file_system_object.saveFile("data.json", self.address_book_object)
            print("\n\t-------  successfully created new address book --------\n")

        elif choice1 == 4:
            self.address_book_object.printAll()

    def create_address_book(self):
        self.file_system_object.saveFile(
            "address.json", self.create_address_book_object)
        print("\n\t-------  successfully created  --------\n")

    def quit_application(self):
        return False

    def read_person(self):
        return {
            'firstname': input("enter firstname : "),
            'lastname': input("enter lastname : "),
            'address': input("enter address : "),
            'city': input("enter city : "),
            'state': input("enter state : "),
            'zipcode': input("enter zipcode : "),
            'phonenumber': input("enter phonemuber : ")
        }

    def add(self, address_book_object_call, file_system_object):

        address_book_object_call.addPerson(Person(self.read_person()))
        file_system_object.saveFile("data.json", address_book_object_call)
