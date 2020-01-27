"""

    @file system handiles the json file

"""

import json
from doctor import Doctor
from patient import Patient
from clinic_manager import Management


class FileSystem:

    def readFile(self, file_name):
        doctors_list = []
        patients_list = []

        with open(file_name, 'r') as file_list:
            data = json.load(file_list)
            for doctor_dict in data['doctors']:
                doctors_list.append(Doctor(doctor_dict))

            for patients_dict in data['patients']:
                patients_list.append(Patient(patients_dict))

            management_object = Management(doctors_list, patients_list)

        return management_object

    def saveFile(self, file_name, management_object):
        with open(file_name, 'w') as file_list:
            json.dump(management_object.to_dict(), file_list, indent=4)