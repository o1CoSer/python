lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for item in lista:
         print(item, end=" ")

listaabecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]         
listaiteraciones = [1,2,3,4,5]
for item in listaiteraciones:
    print("iteracion numero: " + str(item))
    for letra in listaabecedario:
        print(letra, end=" ")
        print("\n")

lista = [99, "casa", ["hola","adios"], "perro", "gato",34]
for item in lista:
    print(item)

for item in range(5):
    for item2 in range(3):
        print("Iteración" + str(item) + "," + str(item2))

i=0
while i<10:
   print(i,end="")
   i=i+1


pedirnumero = True
while pedirnumero:
    valor = int(input("Introduce un entero inferior a 10: "))
    if valor<10:
        pedirnumero = False
print("FIN: ¡Ha introducido un valor inferior a 101!")

item1 = 0
while item<5:
    item2=0
    while item2<3:
       print("Interación" + str(item1) + "," + str(item2))
       item2 = item2 + 1
    item1 = item1 + 1

for item1 in range(5):
    item2 = 0
    while item2<3:

        print("Iteración" + str(item1) + "," + str(item2))
        item2 = item2 + 1
        

    

                
    
                  


    
    
