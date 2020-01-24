from person import Person


class AddressBook:

    def __init__(self, collection=[], count=0, file_name=None):
        self.__collection = collection
        self.__count = count
        self.__file_name = file_name

    def getNumberOfPersons(self):
        return self.__count

    def addPerson(self, Person):

        self.__collection.append(Person)
        self.__count += 1

    def updatePerson(self, index, address, city, state, zip_code, phone_number):

        pass

    def removePerson(self, index):
        pass

    def printAll(self):
        for index in range(len(self.__collection)):
            print(self.__collection[index])

        print(self.__count)
        print(self.__file_name)

    def sortByName(self):
        pass

    def sortByZip(self):
        pass

    def getFile(self):
        return self.__file_name

    def getTitle(self):
        pass

    def setFile(self):
        pass

    def to_dict(self):
        person_dict_list = []
        for person_obj in self.__collection:
            person_dict_list.append(person_obj.to_dictionary())

        return {'persons': person_dict_list, "count": self.__count, "file_name": self.__file_name}
