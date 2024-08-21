import tkinter as tk
ventana = tk.Tk()

ventana.title('Mi ventana')
ventana.geometry('600x800')
ventana.configure(bg='pale green')

#Crear un frame
frame1 = tk.Frame(ventana)
frame1.configure(width=300, height=200, bg="peach puff", bd=5)
frame2 =  tk.Frame(frame1)
frame2.configure(width=100, height=100, bg="cyan", bd=5)

#Crear un boton dentro de frame1
boton = tk.Button(frame1, text='Hola')

frame2.pack()
frame1.pack()
boton.pack()

#Crear un Label Frame
labelFrame = tk.LabelFrame(ventana, text='Hola', bg='yellow', pady=10)
labelFrame.configure(width=300, height=200)
labelFrame.pack()
ventana.mainloop()