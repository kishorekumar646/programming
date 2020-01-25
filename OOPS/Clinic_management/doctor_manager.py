
class Doctors:

    def __init__(self,dict_doctors={}):
        self.__name = dict_doctors['name']
        self.__id_number = dict_doctors['id_number']
        self.__specialization = dict_doctors['specialization']
        self.__avaliability = dict_doctors['avaliability']
        self.__appointment_avaliable = dict_doctors['appointment_avaliable']

    def add_doctor(self,doctor_dict):
        pass

    def print_doctors_list(self):
        pass

    def to_dictionary(self):
        return {
            "name": self.__name,
            "id_number": self.__id_number,
            "specialization": self.__specialization,
            "avaliability": self.__avaliability,
            "appointment_avaliable": self.__appointment_avaliable
        }

    def __str__(self):
        return f"""
            "name" : {self.__name}, 
            "id_number" : {self.__id_number},
            "specialization" : {self.__specialization}, 
            "avaliability" : {self.__avaliability}, 
            "appointment_avaliable" : {self.__appointment_avaliable}
        """
