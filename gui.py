import tkinter
from utils import apply_model, apply_model_from_data
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
ventana.geometry("400x300")

etiqueta_n = tkinter.Label(ventana, text = "N")
caja_texto_n = tkinter.Entry(ventana)
etiqueta_m = tkinter.Label(ventana, text = "M")
caja_texto_m = tkinter.Entry(ventana)
etiqueta_coordenadas = tkinter.Label(ventana, text = "Coordenadas")
caja_texto_coordenadas = tkinter.Entry(ventana)
boton_enviar =tkinter.Button(ventana,text="Click", command=enviar_datos)
respuesta_ubicacion =tkinter.Label(ventana)
respuesta_distancia =tkinter.Label(ventana)
respuesta_tiempo =tkinter.Label(ventana)
boton_abrir =tkinter.Button(ventana,text="Abrir", command=abrir_archivo)

etiqueta_n.pack()
caja_texto_n.pack()
etiqueta_m.pack()
caja_texto_m.pack()
etiqueta_coordenadas.pack()
caja_texto_coordenadas.pack()
boton_enviar.pack()
boton_abrir.pack()
respuesta_ubicacion.pack()
respuesta_distancia.pack()
respuesta_tiempo.pack()


ventana.mainloop()

