import patient,doctor
class User(patient.Patients):
    def search(self):
        while True:
            print(""" Whom do You Wanna Search [1]. Doctors   [2].Patients [0]. Exit""")
            choice = int(input("enter your choice = "))
            if choice == 1:
                Doctor.doc_list(self)
            elif choice ==2:
                Patients.patient_list(self)
            elif choice ==0:
                break

    def check_appointment(self):
        Patients.which_doc(self)

    

if __name__ == "__main__":

    doctor_object = doctor.Doctor()
    patient_object = patient.Patients()

    b = True
    while b:
        print("\n1.Search \t2.Take appointment\t3.Terminate")
        choice = int(input("Enter your choice : "))
        if choice == 1:

            print("\n1.doctors\t2.patients")
            check = int(input("Enter your choice : "))

            if check == 1:
                doctor_object.doc_list()
            elif check == 2:

            else:
                print("Wrong input")
            

# u = User()
# print("""[1]. Search Doctors    [2]. Take Appointment """)
# n = int(input("Choose plss... = "))
# if n == 1:
#     u.search()
# elif n == 2:
#     u.check_appointment()
