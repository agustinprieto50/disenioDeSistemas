from persona import Person

persona = Person('kobe', 'bryant', 38, 'rodeo dr', 10000)

print('name: ', persona.getName())
print('edad: ',persona.getAge())
print('address: ', persona.getDomicilio())
persona.setAge(45)
print('change age: ', persona.getAge())


