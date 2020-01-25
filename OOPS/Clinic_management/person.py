class Person:

    def __init__(self, dict_person={}):
        self.__name = dict_person['name']
        self.__id_number = dict_person['id_number']
        self.__specialization = dict_person['specialization']
        self.__avaliability = dict_person['avaliability']
        self.__appointment_avaliable = dict_person['appointment_avaliable']

    def getName(self):
        return self.__name

    def getIdNumber(self):
        return self.__id_number

    def getSpecialization(self):
        return self.__specialization

    def getAvaliability(self):
        return self.__avaliability

    def getAppointmentAvaliable(self):
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
