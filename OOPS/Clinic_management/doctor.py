
class Doctors:

    def __init__(self,dict_doctors={}):
        self.__name = dict_doctors['name']
        self.__id_number = dict_doctors['id_number']
        self.__specialization = dict_doctors['specialization']
        self.__avaliability = dict_doctors['avaliability']
        self.__appointment_avaliable = dict_doctors['appointment_avaliable']

    def get_name(self):
        return self.__name

    def get_id_number(self):
        return self.__id_number

    def get_specialization(self):
        return self.__specialization
    
    def get_avaliability(self):
        return self.__avaliability(self)

    def get_appointment_avaliable(self):
        return self.__appointment_avaliable

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
