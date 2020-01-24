class Person:

    def __init__(self, dictionary={}):
        self.firstName = dictionary['firstname']
        self.lastName = dictionary['lastname']
        self.address = dictionary['address']
        self.city = dictionary['city']
        self.state = dictionary['state']
        self.zipcode = dictionary['zipcode']
        self.phonenumber = dictionary['phonenumber']

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getAddress(self):
        return self.address

    def getCity(self):
        return self.city

    def getState(self):
        return self.state

    def getZip(self):
        return self.zipcode

    def getPhoneNumber(self):
        return self.phonenumber

    def to_dictionary(self):
        return {
            "firstname": self.firstName,
            "lastname": self.lastName,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "zipcode": self.zipcode,
            "phonenumber": self.phonenumber
        }

    def __str__(self):
        return f"""
            "firstname": {self.firstName},
            "lastname": {self.lastName},
            "address": {self.address},
            "city": {self.city},
            "state": {self.state},
            "zipcode": {self.zipcode},
            "phonenumber": {self.phonenumber}
        """
