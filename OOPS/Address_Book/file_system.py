import json
from person import Person
from address_book import AddressBook


class FileSystem:

    def readFile(self, file_name):
        persons = []
        count = 0
        with open(file_name, 'r') as file_list:
            s = json.load(file_list)
            for person_dict in s['persons']:
                persons.append(Person(person_dict))
                count +=1

            addressbook = AddressBook(persons, count, s['file_name'])

        return addressbook

    def saveFile(self, file_name, address_book_object):
        with open(file_name, 'w') as file_list:
            json.dump(address_book_object.to_dict(), file_list, indent=4)
