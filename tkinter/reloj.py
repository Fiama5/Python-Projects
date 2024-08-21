import tkinter as tk
import time

ventana = tk.Tk()
ventana.title('Ejemplo Label')
ventana.configure(width=600, height=400)
#Crear una etiqueta
etiqueta = tk.Label(ventana, text='Hola soy un label')
#Cambiar fondo, fuente, tamanio
etiqueta.configure(bg='pale green', font=('Arial', 14, 'italic'))
etiqueta.pack()

#Fuincion para mostrar la hora actual
def actualizar_hora():
    #Guarda la hora de ese momento
    etiqueta.config(text=time.strftime('%H:%M:%S'))
    #Actualiza la hora cada 1 segundo
    #Esto llama la funcion actualizar_hora cada 1 segundo
    ventana.after(1000, actualizar_hora)

actualizar_hora()
ventana.mainloop()