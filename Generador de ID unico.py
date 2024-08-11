from random import randint


print('*** Sistema de Generador ID Unico')
nombre = input('Cual es tu nombre?')
apellido = input('Cual es tu apellido?')
nacimiento = input ('En que año naciste?')

random = randint(0,9999)
id = nombre[0:2].upper() + apellido[0:2].upper() + nacimiento [2:4] + str(random)
print(f'Hola {nombre}!')
print(f'Tu numero de identificacion es: {id}')
print('Felicidades!')

