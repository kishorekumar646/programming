from address_book_controller import AddressBookController

if __name__ == "__main__":

    try:

        address_book_controll_object = AddressBookController()
        b = True
        while b:

            print("\n1.Open address book\t2.Create adress book\t3.Quit application\n")
            choice = int(input("Enter your choice : "))

            if choice == 1:

                address_book_controll_object.open_address_book()

            elif choice == 2:
                
                address_book_controll_object.create_address_book()

            elif choice == 3:
                b = address_book_controll_object.quit_application()
                print("\n\t---------- stored data  ----------\n")

            else:
                print("Wrong input!")

    except ValueError:
        print("\n\t-----------  Take integers only  ----------\n")
