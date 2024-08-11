print("***Sistema de Administracion de Cuentas")
salir = False
#Negacion del salir, para que en el ciclo esta en true
while not salir:
    print(f'''Menu:
          1. Crear cuenta
          2. Eliminar cuenta
          3. Salir''' )
    #Transformo el input en un int
    opcion = int(input('Escoje una opcion: '))
    if opcion == 1:
        print('Creando una cuenta...\n')
    elif opcion ==2:
        print('Elimianndo tu cuenta...\n')
    elif opcion == 3:
        print('Saliendo del sistema. Hasta pronto...\n')
        salir = True
    else:
        print('Opcion invalida, seleciona otra opcion...\n')