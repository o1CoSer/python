diassemanaingles={"lunes":"monday",
                  "martes":"tuesday",
                  "miercoles":"wednesday",
                  "jueves":"thrusday",
                  "viernes":"friday"}
print(diassemanaingles["lunes"])
print(diassemanaingles["miercoles"])
print(diassemanaingles["viernes"])

diassemanaingles={"lunes":"monday",
                  "martes":"tuesday",
                  "miercoles":"wednesday",
                  "jueves":"thrusday",
                  "viernes":"friday"}
print(diassemanaingles)
diassemanaingles ["sabado"]="saturday"
print(diassemanaingles)
diassemanaingles ["domingo"]="sunday"
print(diassemanaingles)
diassemanaingles["lunes"]="mondayborrar"
print(diassemanaingles)
del diassemanaingles["lunes"]
print(diassemanaingles)


diassemanaingles={"lunes":"monday",
                  "martes":"tuesday",
                  "miercoles":"wednesday",
                  "jueves":"thrusday",
                  "viernes":"friday"}
print("numero de elementos del diccionario: ",len(diassemanaingles))
print("elemento mayor del diccionario: ",max(diassemanaingles))
print("elemento menor del diccionario: ",min(diassemanaingles))

diassemanaingles={"lunes":"monday",
                  "martes":"tuesday",
                  "miercoles":"wednesday",
                  "jueves":"thrusday",
                  "viernes":"friday"}
print("diccionario original: ",diassemanaingles)
diccionariocopia=diassemanaingles.copy()
print("diccionario copy: ",diccionariocopia)
print("valor del lunes (pop): ",diassemanaingles.pop("lunes"))
print("diccionario despues del pop: ",diassemanaingles)
print("elemento al azar con popitem: ",diassemanaingles.popitem())
print("diccionario despues del popitem: ",diassemanaingles)
print("valor del martes (get): ",diassemanaingles.get("martes"))
print("valor del lunes (get) (no existe): ",diassemanaingles.get("lunes"))
print("valor del lunes (get) (no existe): ",diassemanaingles.get("lunes","no existe"))
diassemanaingles.update({"lunes": "mondayNUEVO","martes":"tuesdayNUEVO"})
print("diccionario despues del update: ",diassemanaingles)
print("setdefault del sabado: ",diassemanaingles.setdefault("sabado","saturday"))
print("diccionario despues del setdefault (nuevo elemento): ",diassemanaingles)
print("setdefault del lunes: ",diassemanaingles.setdefault("lunes","lunes"))
print("diccionario despues del setdefault (elemento existente): ",diassemanaingles)
print("elemento iterable(items): ",diassemanaingles.items())
print("elemento iterable (claves): ",diassemanaingles.keys())
print("elemento iterable (valores): ",diassemanaingles.values())
print("diccionario despues del clear: ",diassemanaingles.clear())

