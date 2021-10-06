class Address():
    def __init__(self, street=None, number=None):
        self.street = street
        self.number = number

    def setStreet(self, value):
        self.street = value
    
    def getStreet(self):
        return self.street
    
    def setNumber(self, value):
        self.number = value

    def getNumber(self):
        return self.number

    