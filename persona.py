class Persona:
    #Constructor
    def __init__(self, nombre, apellido):
        self._nombre = nombre #Atributo protegido
        self.__apellido = apellido #Atributo privado

    def mostrar_persona(self):
        print(f'Persona: nombre = {self.apellido}, apellido = {self.apellido}')


persona1 = Persona('Fiama', 'Arrua')
persona1.mostrar_persona()