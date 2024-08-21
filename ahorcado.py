import random

frutas = ["manzana", "banana", "naranja", "uva", "pera"]
verduras = ["zanahoria", "espinaca", "brócoli", "tomate", "cebolla"]
marcas_tecnologias = ["Apple", "Samsung", "Microsoft", "Google", "Sony"]
utiles_escolares = ["cuaderno", "lápiz", "borrador", "regla", "tijeras"]
animales = ["perro", "gato", "elefante", "tigre", "pájaro"]
comidas = ["pizza", "sushi", "hamburguesa", "ensalada", "pastel"]

categorias = [
    {"nombre": "Frutas", "elementos": frutas},
    {"nombre": "Verduras", "elementos": verduras},
    {"nombre": "Marcas de Tecnología", "elementos": marcas_tecnologias},
    {"nombre": "Útiles Escolares", "elementos": utiles_escolares},
    {"nombre": "Animales", "elementos": animales},
    {"nombre": "Comidas", "elementos": comidas}
]

x = random.choice(categorias)
y = random.choice(x['elementos']).lower()

nro_caracter = len(y)

nro_oportunidades = nro_caracter + 2

adivinadas = ['_'] * len(y)
cont = 0

print('---------------------------------------------')
print('Bienvenido al juego del ahorcado')
print('---------------------------------------------')
print(f'Tu palabra a adivinar es de la categoria {x['nombre']}')
print(y)


def mostrar_palabra(adivinadas):
    return " ".join(adivinadas)

incorrecta = False
while cont < nro_oportunidades:

    letra = input(f'Ingrese una letra, tu nro de oportunidades es de {nro_oportunidades}').lower()
    letra.lower()
    print(mostrar_palabra(adivinadas))
    
    
    if incorrecta == True:
        nro_oportunidades -= 1
        print('Usted ingreso una letra incorrrecta o ya ingresada')

    for i in range(len(y)):
        if letra == y[i]:
            adivinadas[i] = letra
            incorrecta = False
            
        elif letra != y[i]:
            incorrecta = True
        
        elif letra == adivinadas[i]:
            incorrecta = True
    cont += 1


