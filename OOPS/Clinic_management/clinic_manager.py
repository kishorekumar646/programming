"""
    Clinic manager manage doctors and patients

"""
from doctor import Doctor
from patient import Patient

class Management:

    def __init__(self, doctors_collection=[], patients_collection=[]):
        self.__doctors_collection = doctors_collection
        self.__patients_collection = patients_collection

    def remove_doctor(self, id_number):
        doctor_list = []
        flag = False
        for doctor in self.__doctors_collection:
            doctor_list.append(doctor.to_dictionary())
        for index in range(len(doctor_list)):
            if doctor_list[index]['id_number'] == id_number:
                del self.__doctors_collection[index]
                flag = True
        return flag

    def remove_patient(self, id_number):
        patient_list = []
        flag = False
        for patient in self.__patients_collection:
            patient_list.append(patient.to_dictionary())
        for index in range(len(patient_list)):
            if patient_list[index]['id_number'] == id_number:
                del self.__patients_collection[index]
                flag = True
        return flag

    def add_doctor(self, new_doctor):
        new_doctor = Doctor(new_doctor)
        self.__doctors_collection.append(new_doctor)

    def add_patient(self, new_patient):
        new_patient = Patient(new_patient)
        self.__patients_collection.append(new_patient)

    def print_doctor_list(self):
        for index in range(len(self.__doctors_collection)):
            print(self.__doctors_collection[index])

    def print_patient_list(self):
        for index in range(len(self.__patients_collection)):
            print(self.__patients_collection[index])

    def to_dict(self):
        patient_dict_list = []
        doctor_dict_list = []
        for doctor_obj in self.__doctors_collection:
            doctor_dict_list.append(doctor_obj.to_dictionary())

        for patient_obj in self.__patients_collection:
            patient_dict_list.append(patient_obj.to_dictionary())

        return {'doctors': doctor_dict_list, 'patients': patient_dict_list}
