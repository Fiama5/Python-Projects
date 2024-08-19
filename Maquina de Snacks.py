productos = [
    {
        "id": "1",
        "Nombre": "Papas",
        "Precio": 170
    },
    {
        "id": "2",
        "Nombre": "Coca Cola",
        "Precio": 250
    },
    {
        "id": "3",
        "Nombre": "Sandwich",
        "Precio": 400
    },
    {
        "id": "4",
        "Nombre": "Chocolate",
        "Precio": 100
    }
]

salir = True
items = []
total = 0
while salir:
    print('''\nMenu:
    1. Comprar Snack
    2. Mostrar ticket
    3. Salir''')
    
    nro = int(input('Ingrese el número de la operación que desea realizar: '))
    
    if nro == 1:
        print('Productos disponibles:')
        for producto in productos:
            print(f'id: {producto["id"]} - {producto["Nombre"]} - Precio: ${producto["Precio"]}')
        
        nro2 = int(input('Ingresa el número del snack que deseas comprar: '))
        
        if 1 <= nro2 <= len(productos):
            items.append(productos[nro2 - 1])
            print('Item ingresado correctamente.')
            total += productos[nro2 - 1]["Precio"]
        
        else:
            print('Número de snack no válido.')
    
    elif nro == 2:
        if len(items) > 0:
            print('Su ticket es:')
            for item in items:
                print(f'{item["Nombre"]} - ${item["Precio"]}')
            print(f'Total = {total}')
            salir = False
        else:
            print('No hay productos en su ticket.')
    
    elif nro == 3:
        print('Saliendo del sistema.')
        salir = False
    
    else:
        print('Opción inválida.')
