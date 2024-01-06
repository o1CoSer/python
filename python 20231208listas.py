lista=["Coaching","Coach","Coachee","Wingwave","Zero"]
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])

lista1=["Coaching","Coach","Wingwave","Zero","PNL"]
lista2=["Python","IA","PLN","SQL","PLAIN","Ingles"]
print("Numero elementos lista1: ",len(lista1))
print("lista1: ", lista1)
print("Numero elementos lista2: ",len(lista2))
print("lista2: ", lista2)
listaconcatenada=lista1+lista2
print("Numero elementos de listaconcatenada: ",len(listaconcatenada))
print("listaconcatenada: ",listaconcatenada)

lista=["Python", "IA", "PLN", "SQL", "PLAIN", "Ingles"]
print(lista)
lista=lista+["Excel"]
print(lista)
lista=lista+["PowerPoint", "Cyberseguridad"]
print(lista)
lista=lista+["ChatGPT"] + ["TensorFlow"]             
print(lista)

lista=["Python", "PLN", "IA", "SQL"]
print(lista)
lista[1]="Coaching"
print(lista)
del lista[0]
print(lista)

lista=["Python", "PLN", "SQL"]
print(lista)
listaresultante=lista*3
print(listaresultante)

lista=["Python", "PNL", "IA", "SQL"]
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[1][0])
print(lista[1][1])

lista=[1,2,3,4,5,6,7,8,9]
print(lista)
lista1=lista[3:7]
print(lista1)
lista2=lista[:5]
print(lista2)
lista3=lista[6:]
print(lista3)

lista=[45,32,3,78]
print("lista original: ",lista)
lista.append(995)
lista.append(7)
print("lista despues de usar append: ",lista)
lista.sort()
print("lista ordenada: ",lista)
lista.reverse()
print("lista al reves: ",lista)
listaextend=[1,5,87,45]
lista.extend(listaextend)
print("lista despues de extend: ",lista)
lista.sort(reverse=True)
print("lista ordenada al reves: ",lista)
print("numero de elementos 45: ",lista.count(45))
lista.insert(4,111)
print("lista despues de insert: ",lista)
lista.remove(45)
print("lista despues de remove: ",lista)
print("posicion del elemento 111: ",lista.index(111))
lista.pop()
print("lista despues de pop: ",lista)
lista.clear()
print("lista despues de clear: ",lista)





      















