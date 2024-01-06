def Hola():
    print("¡Hola! ¿te está gustando Python?")
print("Primera invocación: ", end="")
Hola()
print("Segunda invocación: ", end="")
Hola()

def Hola():
    return "¡Hola! ¿te está gustando Python?"
print("Primera invocación: " + Hola())
print("Segunda invocación: " + Hola())

def EsParOImpar(param):
    if param%2 == 0:
        print("el número es par")
    else:
        print("el número es impar")

numero = int(input("Introduce un número:"))
EsParOImpar(numero)

# una función que realice una multiplicación de dos valores pasados como parámetros y devuelva el resultado de dicha multiplicación

def Multiplicar(param1, param2):
    return param1 * param2

multiplicando =int(input("Introduce el multiplicando: "))
multiplicador =int(input("Introduce el multiplicador: "))
resultado = Multiplicar(multiplicando, multiplicador)
print("El resultado de la multiplicación es: ", resultado)


# Cómo se le puede pasar a una función de Python un número variable de parámetros de entrada

def Sumar(*valores):
    resultado = 0
    for item in valores:
        resultado = resultado + item
    return resultado
    
resultado = Sumar(3,87,45,63,345,3,58,33,22,11,99)
print("El resultado de la suma es: ", resultado)


# Aprender que con la sentencia return es posible devolver más de un valor.

def SumarMultiplicar(*valores):
    resultadosuma = 0
    resultadomultiplicacion = 1
    for item in valores:
        resultadosuma = resultadosuma + item
        resultadomultiplicacion = resultadomultiplicacion * item
    return resultadosuma,resultadomultiplicacion

ressuma,resmulti = SumarMultiplicar(3,87,45,63,345,3,58,33,22,11,99)
print("El resultado de la suma es: ", ressuma)
print("El resultado de la multiplicacion es: ", resmulti)


# Utilizar funciones dentro de otras funciones

def SumarMultiplicar(param1, param2):
    return Sumar(param1,param2), Multiplicar(param1,param2)

def Sumar(sumando1, sumando2):
    return sumando1 + sumando2

def Multiplicar(multiplicando, multiplicador):
    return multiplicando * multiplicador
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
resultadosuma, resultadomultiplicacion = SumarMultiplicar(numero1, numero2)
print("El resultado de la suma es: ", resultadosuma)
print("El resultado de la multiplicacion es: ", resultadomultiplicacion)


# Funciones con variables globales

def Variables():
    variable = 3
    print("Valor dentro de la función: " + str(variable))

variable = 5
Variables()
print ("Variable en el programa principal: " + str(variable))

def Variables():
    global variable
    print("Valor dentro de la función: " + str(variable))
    variable = 3
    print("Valor dentro de la función: " + str(variable))

variable = 5
print("Variable en el programa principal: " + str(variable))
Variables()
print("Variable en el programa principal: " + str(variable))






