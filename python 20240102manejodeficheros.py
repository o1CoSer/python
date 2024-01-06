
f = open('fichero.txt', 'r')
texto = f.read()
print(texto)
f.close()

for linea in open('fichero.txt', 'r'):
    print(linea)
    
          
