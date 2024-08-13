print('Cajero Automático')
salir = False
saldo = 10000

while not salir:
    print('''¿Qué operación deseas realizar?
    1. Consultar saldo
    2. Retirar
    3. Depositar
    4. Salir''' )

    opcion = int(input('¿Cuál opción escoges? '))
    
    if opcion == 1:
        print(f'Tu saldo es de {saldo}\n')

    elif opcion == 2:
        retiro = int(input('¿Cuánto saldo deseas retirar? '))
        if retiro <= saldo:
            saldo -= retiro
            print(f'''Tu retiro fue exitoso.
            Tu saldo actual es de {saldo}\n''')
        else: 
            print(f'''Dinero insuficiente
                  Tu saldo es de {saldo}\n''')

    elif opcion == 3:
        deposito = int(input('¿Cuánto dinero deseas depositar? '))
        saldo += deposito
        print(f'''Tu depósito fue exitoso.
        Tu saldo actual es de {saldo}\n''')

    elif opcion == 4:
        salir = True
        print('Gracias por usar el cajero automático. ¡Hasta luego!')

    else:
        print('Opción inexistente\n')
