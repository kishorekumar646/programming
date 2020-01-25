
from doctor_manager import Doctors
from patient_manager import Patients

class Management:

    def __init__(self,doctors_collection=[],patients_collection=[]):
        self.__doctors_collection = doctors_collection
        self.__patients_collectio = patients_collection

    def read_docter(self):
        return {
            "name": input("Enter name : "),
            "id_number": input("Enter id number : "),
            "specialization": input("Enter specializations : "),
            "avaliability": input("Enter avaliability or not(yes/no) : "),
            "appointment_avaliable": 0
        }
    
    def read_patient(self):
        return {
            "name": input("Enter your name : "),
            "id_number": input("Enter id number : "),
            "mobile_number": input("Enter mobile number : "),
            "age": input("Enter age : ")
        }
    def add_doctor(self):
        new_doctor = Doctors(self.read_docter())
        self.__doctors_collection.append(new_doctor)

    def add_patient(self):
        new_patient = Patients(self.read_patient())
        self.__patients_collectio.append(new_patient) 

    def print_doctor_list(self):
        for index in range(len(self.__doctors_collection)):
            print(self.__doctors_collection[index])

    def print_patient_list(self):
        for index in range(len(self.__patients_collectio)):
            print(self.__patients_collectio[index])

    def to_dict(self):
        patient_dict_list = []
        doctor_dict_list = []
        for doctor_obj in self.__doctors_collection:
            doctor_dict_list.append(doctor_obj.to_dictionary())

        for patient_obj in self.__patients_collectio:
            patient_dict_list.append(patient_obj.to_dictionary())

        return {'doctors': doctor_dict_list,'patients': patient_dict_list}

    

