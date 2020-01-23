import person

class AddressBook(person.Person):

    def __init__(self):
        self.__collection = []
        self.__count = 0
        self.__file = "data.json"
        self.__changedSinceLastSave = True

    def getNumberOfPersons(self):
        pass

    def addPerson(self,id_number,first_name,last_name,address,city,state,zip_code,phone_number):

        super().__init__(id_number,first_name,last_name,address,city,state,zip_code,phone_number)
        self.__count += 1
        return self.toString()
        
    def updatePerson(self,index,address,city,state,zip_code,phone_number):
        
        pass
    def removePerson(self,index):
        pass

    def sortByName(self):
        pass

    def sortByZip(self):
        pass

    def getFile(self):
        return self.__file

    def getTitle(self):
        pass

    def setFile(self):
        pass

    def getChangedSinceLastSave(self):
        pass

    def setChangedSinceLastSave(self):
        pass




