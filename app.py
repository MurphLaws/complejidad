from flask import Flask
from minizinc import Instance, Model, Solver
from flask import Flask


universidad = Model("./Universidad.mzn")
gecode = Solver.lookup("gecode")
instance = Instance(gecode, universidad)

instance["n"] = 10
instance["m"] = 10
instance["ciudades"] = [[0,1],[2,4],[3,8],[4,1],[6,3],[6,4],[6,5],[8,7],[9,3],[9,10]]


result = str(instance.solve())
print(result)



