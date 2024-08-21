class Monitor:
    contador_monitor = 0
    def __init__(self, marca, tamanio):
        self.marca = marca
        self.tamanio = tamanio
        Monitor.contador_monitor += 1
        self.id_monitor = Monitor.contador_monitor
    def __str__(self):
        return (f'Id: {self.id_monitor}, Marca: {self.marca}, Tamanio: {self.tamanio}')
        
# monitor1 = Monitor('Samsung', '17')
# print(monitor1)