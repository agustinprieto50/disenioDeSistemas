from persona import Person


class Student(Person):
    def __init__(self, name, surname, matricula):
        super().__init__(name, surname)
        self.matricula = matricula


