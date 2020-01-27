from file_system import FileSystem
from clinic_manager import Management

"""
    Evaluate clinic management application

"""

def read_docter():
    return {
        "name": input("Enter name : "),
        "id_number": input("Enter id number : "),
        "specialization": input("Enter specializations : "),
        "avaliability": "yes",
        "appointment_avaliable": 0
    }

def read_patient():
    return {
        "name": input("Enter your name : "),
        "id_number": input("Enter id number : "),
        "mobile_number": input("Enter mobile number : "),
        "age": input("Enter age : ")
    }

if __name__ == "__main__":

    try:

        management_object = Management()
        file_system_object = FileSystem()

        b = True
        while b:
            print("\n1.Manage doctors\t2.Manage patient\t3.Take appointment\t4.Terminate")
            choice = int(input("Enter your choice : "))
            if choice == 1:

                management_object = file_system_object.readFile("clinic.json")

                print("1.add\t2.update\t3.delete\t4.search\t5.print_data")
                choice1 = int(input("Enter your choice : "))

                if choice1 == 1:
                    management_object.add_doctor(read_docter())
                    file_system_object.saveFile(
                        "clinic.json", management_object)

                elif choice1 == 2:
                    pass

                elif choice1 == 3:
                    id_number = input("Enter id number : ")
                    if management_object.remove_doctor(id_number):
                        file_system_object.saveFile(
                            "clinic.json", management_object)
                        print("\n\t-------  successfully delete --------\n")
                    else:
                        print("Not found id number")

                elif choice1 == 4:
                    pass

                elif choice1 == 5:
                    management_object.print_doctor_list()

                else:
                    print("wrong number")

            elif choice == 2:
                management_object = file_system_object.readFile("clinic.json")

                print("1.add\t2.update\t3.delete\t4.search\t5.print_data")
                choice1 = int(input("Enter your choice : "))
                if choice1 == 1:
                    management_object.add_patient(read_patient())
                    file_system_object.saveFile(
                        "clinic.json", management_object)
                elif choice1 == 2:
                    pass
                elif choice1 == 3:
                    id_number = input("Enter id number : ")
                    if management_object.remove_patient(id_number):
                        file_system_object.saveFile(
                            "clinic.json", management_object)
                        print("\n\t-------  successfully delete --------\n")
                    else:
                        print("Not found id number")
                elif choice1 == 4:
                    pass
                elif choice1 == 5:
                    management_object.print_patient_list()
                else:
                    print("wrong number")

            elif choice == 3:
                pass

            elif choice == 4:
                b = False
                print("\n\t---------- stored data  ----------\n")

    except ValueError:
        print("Wrong input!")
