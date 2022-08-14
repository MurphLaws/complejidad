
from minizinc import Instance, Model, Solver

def apply_model(n,m,ciudades):
    universidad = Model("./Universidad.mzn")
    gecode = Solver.lookup("gecode")
    instance = Instance(gecode, universidad)

    instance["n"] = n
    instance["m"] = m
    instance["ciudades"] = ciudades
    #ejemplo: [[0,1],[2,4],[3,8],[4,1],[6,3],[6,4],[6,5],[8,7],[9,3],[9,10]]


    result = instance.solve()
    return("Ubicación de la universidad (E,N): "+ str(result.solution.ubicacion), "Distancia más larga: "+ str(result.solution.objective))


print(apply_model(10,10,[[0,1],[2,4],[3,8],[4,1],[6,3],[6,4],[6,5],[8,7],[9,3],[9,10]])) 
#def funcion_ejemplo(n,m,coordenadas):
#    print("ESte es N: "+ n + " Este es M: "+ m + " Estas son las coordenadas: "+ coordenadas)