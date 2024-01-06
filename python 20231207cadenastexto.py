cadena1="Sesión de coaching"
cadena2="PNL"
print (cadena1)
print(cadena2)

cadena="Sesión de coaching"
print("Caracter posición 0:",cadena[0])
print("Caracter posición 1:",cadena[1])
print("Caracter posición 2:",cadena[2])
print("Caracter posición 3:",cadena[3])
print("Caracter posición 4:",cadena[4])
print("Caracter posición 5:",cadena[5])

cadena1=input("Introduzca la primera cadena:")
cadena2=input("Introduzca la segunda cadena:")
cadena3=input("Introduzca la tercera cadena:")
cadenasuma=cadena1+""+cadena2+""+cadena3
cadenamultiplicacion=(cadena2+"")*5
print("cadena concatenada",cadenasuma)
print("caracter multiplicada",cadenamultiplicacion)

cadena1=input("Introduzca la primera cadena:")
cadena2=input("Introduzca la segunda cadena:")
cadena3=input("Introduzca la tercera cadena:")
cadenasuma =cadena1
cadenasuma +=""
cadenasuma +=cadena2
cadenasuma +=""
cadenasuma +=cadena3
print("Cadena concatenada:",cadenasuma)

cadena1=input("Introduzca la primera cadena:")
cadena2=input("Introduzca la segunda cadena:")
print("¿Está la segunda cadena contenida en la prinmera?:",cadena2 in cadena1)

cadena1=input("Introduzca la primera cadena:")
cadena2=input("Introduzca la segunda cadena:")
cadena3=input("Introduzca la tercera cadena:")
cadenaconsaltos="\n\t"+cadena1+"\n\t"+cadena2+"\n\t"+cadena3
print("Cadena con saltos:",cadenaconsaltos)
  
cadena1=input("Introduzca la primera cadena:")
cadena2=input("Introduzca la segunda cadena:")
cadena3=input("Introduzca la tercera cadena:")
print("Longitud de la cadena2 (len)",len(cadena2))
print("cadena3 toda a mayusculas (upper):",cadena3.upper())
print("cadena3 toda a minusculas (lower):",cadena3.lower())
print("cadena2 cambia de mayusculas a minusculas y viceversa(swapcase):",cadena2.swapcase())
print("cadena1 la primera a mayusculas (capitalize):",cadena1.capitalize())
print("cadena2 la primera de cada palabra a mayusculas(title):",cadena2.title())
print("¿cadena1 todo minusculas? (islower):",cadena1.islower())
print("¿cadena3 todo mayusculas? (isupper):",cadena3.isupper())
print("¿cadena2 todo caracteres imprimibles? (isprintable):",cadena2.isprintable())
print("¿cadea3 todo valores alfanumericos? (isalnum):",cadena3.isalnum())
print("¿cadena1 todo valores alfabeticos? (isalpha):",cadena1.isalpha())
print("¿cadena3 la primera de cada palabra en mayusculas y el resto minusculas (istitle):",cadena3.istitle())
print("¿cadena2 todos los caracteres son espacios en blanco? (isspace):",cadena2.isspace())
print("¿cadena1 todo digitos? (isdigit):",cadena1.isdigit())
print("¿cadena2 todos los caracteres con representacion numerica? (isnumeric):",cadena2.isnumeric())
print("¿cadena3 todos los caracteres son numeros con representacion decimal? (isdecimal):",cadena3.isdecimal())
print("caracter mas alto de la cadena1 (max):",max(cadena1))
print("caracter mas bajo de la cadena3 (min):",max (cadena3))

cadena=input("Introduzca una cadena con espacios en blanco al principio y al final:")
print("Longitud de la cadena:",len(cadena))
cadenalstrip=cadena.lstrip()
print("cadena (lstrip):",cadenalstrip,end=".")
print("\nlongitu de la cadena (lstrip):",len(cadenalstrip))
cadenarstrip=cadena.rstrip()
print("cadena(rstrip):",cadenarstrip,end=".")
print("\nlongitud de la cadena (rstrip):",len(cadenarstrip))
cadenastrip=cadena.strip()
print("cadena (strip):",cadenastrip,end=".")
print("\nlongitud de la cadena (strip):",len(cadenastrip))

cadena1=input("Introduzca la primera cadena:")
cadena2=input("Introduzca la segunda cadena:")
cadena3=input("Introduzca la tercera cadena:")
cadenaconsaltos=r"\n\t"+cadena1+r"\n\t"+cadena2+r"\n\t"+cadena3
print("Cadena con saltos:",cadenaconsaltos)

cadena=input("Sesión de coaching:")
buscar=input("Sesión de PNL:")
print("¿Comienza coaching a buscar? (startswith):",cadena.startswith(buscar))
print("¿Termina coaching a buscar? (endswitch):",cadena.endswith(buscar))
print("¿Cuantas veces coaching a buscar? (count):",cadena.count(buscar))
      
cadena1=input("Introduzca la primera cadena:")
cadena2=input("Introduzca la segunda cadena:")
cadena3=input("Introduzca la tercera cadena:")
print("¿comienza la cadena por la cadena a buscar? (startswith):",cadena.startswith(buscar))
print("¿termina la cadena por la cadena a buscar? (endswith):",cadena.endswith(buscar))
print("¿cuantas veces aparece la cadena a buscar en la cadena? (count):",cadena.count(buscar))
  
cadena=input("Introduzca una cadena Sesión de coaching:")
buscar=input("Introduzca una cadena para buscar Coachee:")
print("La cadena aparece en la posicion (find):",cadena.find(buscar))
print("La cadena aparece en la posicion (rfind):",cadena.rfind(buscar))

cadena=input("Introduzca una cadena:")
reemplazar=input("Introduzca una subcadena de la anterior para reemplazar:")
reemplazo=input("Introduzca una cadena por la que se reemplazara la anterior:")
print("cadena original:",cadena)
print("cadena nueva(replace):",cadena.replace(reemplazar, reemplazo))
            
cadena=input("Introduzca una cadena con varias palabras:")
print("cadena dividida por espacios en blanco (split):",cadena.split())
 
cadena="Coaching,coachee,coach"
print("Recurso(cadena[11:11]):",cadena[11:11])
print("usuario(cadena[1:10]):",cadena[1:10])
print("profesional(cadena[10:1]):",cadena[10:1])
print("Desde el principio cadena[:11]):", cadena[:11])
print("Desde el final (cadena[:11]):", cadena[10:])
      
multiplicando=int(input("multiplicando:"))
multiplicador=int(input("multiplicador:"))
print("el resultado de multiplicar %d por %d es %d" % (multiplicando, multiplicador, multiplicando*multiplicador))

multiplicando=int(input("multiplicando:"))
multiplicador=int(input("multiplicador:"))
print("El resultado de multiplicar {0} por {1} es {2}" .format(multiplicando,multiplicador,multiplicando*multiplicador))
      

      













