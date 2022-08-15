import tkinter
from test import apply_model, apply_model_from_data
from tkinter import filedialog

def enviar_datos():
    texto_n = caja_texto_n.get()
    texto_m = caja_texto_m.get()
    texto_coordenadas = caja_texto_coordenadas.get()
    respuestas = apply_model(texto_n,texto_m,texto_coordenadas)
    respuesta_ubicacion["text"]= respuestas[0]
    respuesta_distancia["text"]= respuestas[1]
    respuesta_tiempo["text"]= respuestas[2]

def abrir_archivo():
    archivo =filedialog.askopenfilename(title="Abrir")
    respuestas_2 = apply_model_from_data(archivo)
    respuesta_ubicacion["text"]= respuestas_2[0]
    respuesta_distancia["text"]= respuestas_2[1]
    respuesta_tiempo["text"]= respuestas_2[2]

ventana = tkinter.Tk()
ventana.title('Complejidad y Optimización')
ventana.geometry("400x300")

etiqueta_n = tkinter.Label(ventana, text = "N", font=("Helvetica", 12, "bold"))
caja_texto_n = tkinter.Entry(ventana)
etiqueta_m = tkinter.Label(ventana, text = "M", font=("Helvetica", 12, "bold"))
caja_texto_m = tkinter.Entry(ventana)
etiqueta_coordenadas = tkinter.Label(ventana, text = "Coordenadas", font=("Helvetica", 12, "bold"))
caja_texto_coordenadas = tkinter.Entry(ventana)
boton_enviar =tkinter.Button(ventana,text="Resolver", command=enviar_datos)
respuesta_ubicacion =tkinter.Label(ventana,text="Ubicación de la universidad (E,N):")
respuesta_distancia =tkinter.Label(ventana,text="Distancia más larga: ")
respuesta_tiempo =tkinter.Label(ventana)
boton_abrir =tkinter.Button(ventana,text="Abrir", command=abrir_archivo)
espacio_blanco = tkinter.Label(ventana)
espacio_blanco1 = tkinter.Label(ventana)
espacio_blanco2 = tkinter.Label(ventana)

etiqueta_n.grid(row=1,column=0)
caja_texto_n.grid(row=1,column=1)
etiqueta_m.grid(row=2,column=0)
caja_texto_m.grid(row=2,column=1)
etiqueta_coordenadas.grid(row=3,column=0)
caja_texto_coordenadas.grid(row=3,column=1)
boton_enviar.grid(row=5,column=1)
boton_abrir.grid(row=5,column=0)
respuesta_ubicacion.grid(row=7,column=0)
respuesta_distancia.grid(row=8,column=0)
respuesta_tiempo.grid(row=9,column=0)
espacio_blanco.grid(row=4,column=0)
espacio_blanco1.grid(row=6,column=0)
espacio_blanco2.grid(row=0,column=0)

ventana.mainloop()

