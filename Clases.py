#Clase de contacto
#Para definir una clase se usa la palabra reservada 'class'
class Contacto:

#Las clases pueden tener atributos y metodos
    def inicializar_contacto(self, 
        nombre, apellido, celular, email):
        self.nombre = nombre
        self.apellido = apellido
        self.celular = celular
        self.email = email

    def mostrar_contacto(self):
        print(f'''Contacto:
              Nombre: {self.nombre}
              Apellido: {self.apellido}
              Celular: {self.celular}
              Email: {self.email}''')
        

#Crear un primer objeto
contacto1 = Contacto()
contacto1.inicializar_contacto('Fiama', 'Arrua', 34621235, 'fiama@gamil.com')
contacto1.mostrar_contacto()