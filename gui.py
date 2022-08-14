import tkinter
from test import funcion_ejemplo

def enviar_datos():
    texto_n = caja_texto_n.get()
    texto_m = caja_texto_m.get()
    texto_coordenadas = caja_texto_coordenadas.get()
    funcion_ejemplo(texto_n,texto_m,texto_coordenadas)

ventana = tkinter.Tk()
ventana.geometry("400x300")
etiqueta_n = tkinter.Label(ventana, text = "N")
caja_texto_n = tkinter.Entry(ventana)
etiqueta_m = tkinter.Label(ventana, text = "M")
caja_texto_m = tkinter.Entry(ventana)
etiqueta_coordenadas = tkinter.Label(ventana, text = "Coordenadas")
caja_texto_coordenadas = tkinter.Entry(ventana)
boton_enviar =tkinter.Button(ventana,text="Click", command=enviar_datos)
etiqueta_n.pack()
caja_texto_n.pack()
etiqueta_m.pack()
caja_texto_m.pack()
etiqueta_coordenadas.pack()
caja_texto_coordenadas.pack()
boton_enviar.pack()

ventana.mainloop()

