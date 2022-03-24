numeros = (50,42,20,30,40,87)
#convertir a lista
listaNumeros = list(numeros)
#recorro lista a lista
listaNumerosPares=[]
for numero in listaNumeros:
    if(numero % 2 == 0):
        listaNumerosPares.append(numero)
print (listaNumerosPares)
