from domicilio import Address


class Person():
    def __init__(self, name=None, surname=None, age=None, street=None, number=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.domicilio = Address(street, number)

    def setName(self, value):
        self.name = value
    
    def getName(self):
        return self.name
    
    def setSurname(self, value):
        self.surname = value
    
    def getSurname(self):
        return self.surname

    def setAge(self, value):
        self.age = value
    
    def getAge(self):
        return self.age
    
    def setDomicilio(self, value):
        self.domicilio = value
    
    def getDomicilio(self):
        return self.domicilio
    
    
    
    
        
    