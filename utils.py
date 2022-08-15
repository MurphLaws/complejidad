
from minizinc import Instance, Model, Solver
import time
start_time = time.time()




def apply_model(n,m,ciudades):

<<<<<<< HEAD:test.py
    return("Ubicación de la universidad (E,N): ", "Distancia más larga: ","Distancia más larga: ")

def apply_model_from_data(path):

    return("Ubicación de la universidad (E,N): ", "Distancia más larga: ","Distancia más larga: ")
=======
    instance["n"] = int(n)
    instance["m"] = int(m)
    
    parejas = ciudades.split("|")
    matrix = [list(map(int, t.split(","))) for t in parejas]
    instance["ciudades"] = matrix
    result = instance.solve()
    ubicacion_respuesta = [x / 100 for x in result.solution.ubicacion]
    return("Ubicación de la universidad (E,N): "+ str(ubicacion_respuesta), "Distancia más larga: "+ str(result.solution.objective/100), str(round(time.time() - start_time, 2)) + " Segundos")

def apply_model_from_data(path):
    universidad = Model("./Universidad.mzn")
    universidad.add_file(path)
    gecode = Solver.lookup("gecode")
    instance = Instance(gecode, universidad)
    result = instance.solve()
    ubicacion_respuesta = [x / 100 for x in result.solution.ubicacion]
    return("Ubicación de la universidad (E,N): "+ str(ubicacion_respuesta), "Distancia más larga: "+ str(result.solution.objective/100), str(round(time.time() - start_time, 2)) + " Segundos")
>>>>>>> e8335ffaca1da6a18c0dbffa99b738c2cb17519f:utils.py

#print(apply_model_from_data("C:/Users/GAMER/Documents/complejidad/med3.dzn"))