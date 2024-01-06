numero=int(input("escriba un numero del 1 al 1000: "))
if numero<400:
    print("¡el numero que has escrito es menor que 400!")
print("has escrito el numero "+str(numero))

cadena = input("introduzca una cadena de texto: ")
if cadena.endswith("a") or cadena.endswith("e") or cadena.endswith("i") or cadena.endswith("o") or cadena.endswith("u"):
    print("¡la cadena de texto acaba en vocal!")
print("has escrito: "+cadena)

numero=int(input("escriba un numero del 1 al 1000: "))
if numero<400:
     print("¡el numero que has escrito es menor que 400!")
else:
     print("¡el numero que has escrito es mayor o igual que 400!")
print("has escrito el numero: " + str(numero))

sumando1 = int(input("Escriba el primer sumando: "))
sumando2 = int(input("Escriba el segundo sumando: "))
resultado = sumando1+sumando2
print("el resultado de la suma es: " + str(resultado))
if resultado%2==0:
    if resultado>=1000:
        print("¡el resultado de la suma es par y mayor o igual que 1000!")
    else:
        print("¡el resultado de la suma es par y menor que 1000!")
else:
    if resultado>=1000:
        print("¡el resultado de la suma es impar y mayor o igual que 1000!")
    else:
        print("¡el resultado es impar y menor que 1000!")
                        
numero1 = int(input("escriba el primer numero: "))
numero2 = int(input("escriba el segundo numero: "))
if numero1==numero2:
    print("ambos numeros son iguales")
elif numero1>numero2:
    print("¡el primer numero es mayor que el segundo!")
else:
    print("¡el primer numero es menor que el segundo!")
    
    
