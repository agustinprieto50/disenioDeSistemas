from persona import Person
from domicilio import Address


persona = Person('Agu', 'gfsg', 45)
domicilio = Address('fdasasd', 45)


persona.agregateDomicilio(domicilio)

print(persona.getName(), persona.getDomicilio())