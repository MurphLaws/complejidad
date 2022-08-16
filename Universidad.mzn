% Parametros
int: n; % Tamaño de la región.
int: m; % # de ciudades.
set of int: rango=1..n;
set of int: rangoCiudades=1..m;
array[rangoCiudades, 1..2] of 0..n: ciudades;

% Variables
array[rangoCiudades] of var 0..n*2*100: distancias;
array[1..2] of var 0..n*100: ubicacion;

% Definición de distancias
constraint forall(i in rangoCiudades) (
	distancias[i] = abs(100*ciudades[i,1] - ubicacion[1]) + abs(100*ciudades[i,2] - ubicacion[2]));

% Función objetivo
%solve minimize max(distancias);
solve ::int_search(ubicacion, occurrence, indomain_median) minimize max(distancias);
%solve ::int_search(ubicacion, smallest , indomain_min) minimize max(distancias);


output["Ubicación de la universidad (E;N): \(ubicacion[1]/100); "] ++ ["\(ubicacion[2]/100)\n"]++
["Distancia más larga: \(max(distancias)/100)"];

