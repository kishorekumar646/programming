
class Patients:

    def __init__(self,dict_patient={}):
        self.__name = dict_patient['name']
        self.__id_number = dict_patient['id_number']
        self.__mobile_number = dict_patient['mobile_number']
        self.__age = dict_patient['age']        

    def add_patient(self):
        pass

    def print_patient_list(self):
        pass

    def to_dictionary(self):
        return {
            "name": self.__name,
            "id_number": self.__id_number,
            "mobile_number": self.__mobile_number,
            "age": self.__age
        }

    def __str__(self):
        return f"""
            "name" : {self.__name}, 
            "id_number" : {self.__id_number},
            "mobile_number" : {self.__mobile_number}, 
            "age" : {self.__age}
        """