import tkinter as tk

ventana = tk.Tk()
ventana.title('Ejemplo Label')
ventana.configure(width=600, height=400)
#Crear una etiqueta
etiqueta = tk.Label(ventana, text='Hola soy un label')
#Cambiar fondo, fuente, tamanio
etiqueta.configure(bg='pale green', font=('Arial', 14, 'italic'))
etiqueta.pack()

ventana.mainloop()