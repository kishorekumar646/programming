import json
from doctor_manager import Doctors
from patient_manager import Patients
from clinic_manager import Management


class FileSystem:

    def readFile(self, file_name):
        doctors_list = []
        patients_list = []

        with open(file_name, 'r') as file_list:
            data = json.load(file_list)
            for doctor_dict in data['doctors']:
                doctors_list.append(Doctors(doctor_dict))

            for patients_dict in data['patients']:
                patients_list.append(Patients(patients_dict))
    
            management_object = Management(doctors_list,patients_list)

        return management_object

    def saveFile(self, file_name, management_object):
        with open(file_name, 'w') as file_list:
            json.dump(management_object.to_dict(), file_list, indent=4)
# t = FileSystem()
# obj = t.readFile("clinic.json")
# print(obj)