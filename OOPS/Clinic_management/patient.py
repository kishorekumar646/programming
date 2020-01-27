"""
    @patient class 

"""

class Patient:

    def __init__(self,dict_patient={}):
        self.__name = dict_patient['name']
        self.__id_number = dict_patient['id_number']
        self.__mobile_number = dict_patient['mobile_number']
        self.__age = dict_patient['age']        

    def get_name(self):
        return self.__name

    def get_id_number(self):
        return self.__id_number

    def get_mobile_number(self):
        return self.__mobile_number

    def get_age(self):
        return self.__age

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