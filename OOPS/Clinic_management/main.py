from file_system import FileSystem
from clinic_manager import Management


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
                    management_object.add_doctor()
                    file_system_object.saveFile("clinic.json",management_object)
                
                elif choice1 == 2:
                    pass
                
                elif choice1 == 3:
                    index = int(input("Enter index number : "))
                    management_object.remove_doctor(index)
                    file_system_object.saveFile("clinic.json",management_object)
                    print("\n\t-------  successfully delete --------\n")
                
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
                    management_object.add_patient()
                    file_system_object.saveFile("clinic.json",management_object)
                elif choice1 == 2:
                    pass
                elif choice1 == 3:
                    index = int(input("Enter index number : "))
                    management_object.remove_patient(index)
                    file_system_object.saveFile("clinic.json",management_object)
                    print("\n\t-------  successfully delete --------\n")
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
