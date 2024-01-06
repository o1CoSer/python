
# calcular el factorial de un número

def Factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * Factorial(numero-1)
factorial = int(input("Introduzca el número del que quiere calcular el factorial: "))
print("el factorial de " + str(factorial) + " es: " + str(Factorial(factorial)))


# cálculo de la potencia de un número

def Potencia(base, exponente):
    if exponente <=0:
        return 1
    else:
        return base * Potencia(base,exponente-1)

base=int(input("Introduzca la base de la potencia: "))
exponente = int(input("Introduzca el exponente de la potencia: "))
print("El valor de " + str(base) + " elevado a " + str(exponente) + " es: " + str(Potencia(base,exponente)))


