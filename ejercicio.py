numeros = (50,45,20,30,40,87)
#convertir a lista
listaNumeros = list(numeros)
#recorro lista a lista
listaNumerosMayores=[]
for numero in listaNumeros:
    if(numero > 40):
        listaNumerosMayores.append(numero)
print (listaNumerosMayores)

