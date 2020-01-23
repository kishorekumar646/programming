class Person:

    def __init__(self,id_number,first_name,last_name,address,city,state,zip_code,phone_number):
        self.__id = id_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip = zip_code
        self.__phone_number = phone_number
    
    def getFirstName(self):
        return self.__first_name
    
    def getLastName(self):
        return self.__last_name

    def getAddress(self):
        return self.__address

    def getCity(self):
        return self.__city

    def getState(self):
        return self.__state

    def getZip(self):
        return self.__zip

    def getPhoneNumber(self):
        return self.__phone_number

    def toString(self):
        return {
            "id" : self.__id,
            "first_name" : self.__first_name,
            "last_name" : self.__last_name,
            "address" : self.__address,
            "city" : self.__city,
            "state" : self.__state,
            "zip" : self.__zip,
            "phone_number" : self.__phone_number
        }