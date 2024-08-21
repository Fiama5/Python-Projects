import tkinter as tk

#Crear una ventana
ventana = tk.Tk()

#Titulo en la ventana
ventana.title('Mi primera ventana')
#Tamanio de la ventana
ventana.geometry('600x400')
#Poner un icono
ventana.iconbitmap('icons/CoinControl.ico')
#Cambiar color de background
ventana.configure(bg='red')
ventana.minsize(400, 200)

ventana.mainloop()