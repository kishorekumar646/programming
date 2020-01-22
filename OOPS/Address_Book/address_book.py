import json

class Person:

    def __init__(self,first_name,last_name,address,city,state,zip_code,phone_number):
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


class AddressBook:

    def __init__(self):
        self.__collection = []
        self.__count = 0
        self.__file = 0
        self.__changedSinceLastSave = False

    def getNumberOfPersons(self):
        pass

    def addPerson(self,first_name,last_name,address,city,state,zip,phone_number):
        pass

    def getFullNameofPerson(self,index):
        pass

    def getOtherPersonFullInformation(self,index):
        pass

    def updatePerson(self,index,address,city,state,zip,phone_number):
        pass

    def removePerson(self,index):
        pass

    def sortByName(self):
        pass

    def sortByZip(self):
        pass

    def printAll(self):
        pass

    def getFile(self):
        pass

    def getTitle(self):
        pass

    def setFile(self):
        pass

    def getChangedSinceLastSave(self):
        pass

    def setChangedSinceLastSave(self):
        pass


class FileSystem:

    def readFile(self):
        file_list = open('data.json','r')
        s = json.load(file_list)
        file_list.close()

    def saveFile(self):
        pass

if __name__ == "__main__":
    
    file_system = FileSystem()
    file_system.readFile()
    print("Main")