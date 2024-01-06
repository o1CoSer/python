

# Utilizar la sección finally

print ('¡Iniciando el programa!')
print ('\n¡Comenzando primera parte del programa!')
try:
    print(str(17/0))
except:
    print('ERROR: Division por cero')
finally:
    print ('Primera parte de programa acabada!')

print ('\n¡Comenzando segunda parte del programa!')
try:
    print(str(17/1))
except:
    print('ERROR: Dividido por cero')
finally:
    print('¡Segunda parte de programa acabada!')
    
    
        
print('¡Iniciando programa!')
try:
    print(str(17/0))
except ZeroDivisionError:
    print('ERROR: Divisionpor cero')
except:
    print('ERROR: General')
else:
    print('¡Nose han producido errores!')
finally:
    print('¡Programa acabado!')
    
