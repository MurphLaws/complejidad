# Proyecto final Complejidad & Optimización

#### Integrantes
* David Santiago Cortés

* Nicolas Lasso

* Jose Hurtado

* Cesar Becerra

#### Descripción de la entrega
El repositorio contiene todos los archivos requeridos para la ejecución de la entrega del proyecto, el archivo requirements.txt describe los paquetes necesarios para la ejecución del proyecto, se pueden instalar por medio del siguiente comando en pip:
```
pip install -r requirements.txt
```

#### Ejecución del programa

Para ejecutar el programa basta con utilizar el comando desde una terminal en la carpeta del proyecto:

```
python3 ./gui.py
```
La interfaz es sencilla, se pueden ejecutar instancias del problema ya sea cargando archivos .dzn utilizando el botón "abrir" o escribiendo manualmente las instancias, el formato de entrada para las ciudades de seguir la siguiente convención:

```
(coordenadas este ciudad1),(coordenadas norte ciudad1) | (coordenadas este ciudad2), (coordenadas norte ciudad2)....
```
Por ejemplo para definir las ciudades con coordenadas (1,7) y (7,9):
```
1,7|7,9
```
