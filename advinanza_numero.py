import random
print('----------------------------------')
print('Juego de Adivina el numero')
print('----------------------------------')
bajo = int(input('Ingrese el numero mas bajo: '))
alto = int(input('Ingrese el numero alto: '))

x = random.randint(bajo, alto)
salir = True
cont = 0
nro =0
while salir:
    cont += 1
    nro = int(input('Ingrese un numero para adivinar: '))
    if nro > x:
        print('Usted ingreso un numero demasiado alto')
    elif nro < x:
        print('Usted ingreso un numero muy bajo')
    elif nro == x:
        print(f'''***Felicidades***
            Usted adivino el numero {x}''')
        salir = False
    else:
        print('Numero ingresado fuera de los rangos establecidos')

