
from minizinc import Instance, Model, Solver

def apply_model(n,m,ciudades):
    universidad = Model("./Universidad.mzn")
    gecode = Solver.lookup("gecode")
    instance = Instance(gecode, universidad)

    instance["n"] = int(n)
    instance["m"] = int(m)
    
    parejas = ciudades.split("|")
    matrix = [list(map(int, t.split(","))) for t in parejas]
    #'0, 1|2, 4|3, 8|4, 1|6, 3|6, 4|6, 5|8, 7|9, 3|9, 10'
    instance["ciudades"] = matrix
    print(matrix)
    result = instance.solve()
    ubicacion_respuesta = [x / 100 for x in result.solution.ubicacion]
    return("Ubicación de la universidad (E,N): "+ str(ubicacion_respuesta), "Distancia más larga: "+ str(result.solution.objective/100))

def apply_model_from_data(path):
    universidad = Model("./Universidad.mzn")
    universidad.add_file(path)
    gecode = Solver.lookup("gecode")
    instance = Instance(gecode, universidad)
    result = instance.solve()
    ubicacion_respuesta = [x / 100 for x in result.solution.ubicacion]
    return("Ubicación de la universidad (E,N): "+ str(ubicacion_respuesta), "Distancia más larga: "+ str(result.solution.objective/100))

#print(apply_model_from_data("C:/Users/GAMER/Documents/complejidad/med3.dzn"))